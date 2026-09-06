"""One language-model call, cached to disk, so a lab still runs when the network does not.

Week 7's D3 and D4 are the only labs that call a model. Both call it through :func:`chat`,
and everything that makes those labs teachable rather than fragile lives here:

* **Every response is cached** under a hash of the exact request — model, system prompt,
  user prompt, temperature, token limit. Re-running a cell costs nothing and returns the
  same words, so a student can re-read an output without spending a call on it, and a
  measurement taken on Tuesday still holds on Thursday.
* **The cache is looked up before the key is.** A reference set ships in
  ``shared/solutions_cache/llm_cache/``, so the whole of D3 and D4 completes with no key
  and no network. Classroom Wi-Fi fails at least once per cohort; this is the plan for it.
* **A miss with no key is a readable error**, in both languages, naming the prompt that
  missed — not a stack trace out of an HTTP library.

The provider is OpenRouter by default because its free model slugs need no payment method.
Two environment variables move it: ``AIEP_LLM_MODEL`` and ``AIEP_LLM_BASE_URL``. Anything
OpenAI-SDK-compatible works, which includes Google's own endpoint
(``https://generativelanguage.googleapis.com/v1beta/openai/`` with ``gemini-2.0-flash``).

A notebook never contains a key. ``aiep.env.require_key`` reads it from ``.env`` or the
environment, and this module never prints it.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Any

from .paths import notebook_dir, solutions_cache_dir

__all__ = ["chat", "cache_path", "cache_stats", "DEFAULT_MODEL", "DEFAULT_BASE_URL"]

#: A free slug that needs no payment method. Override with AIEP_LLM_MODEL.
DEFAULT_MODEL = os.environ.get("AIEP_LLM_MODEL", "google/gemini-2.0-flash-exp:free")
#: OpenRouter's OpenAI-compatible endpoint. Override with AIEP_LLM_BASE_URL.
DEFAULT_BASE_URL = os.environ.get("AIEP_LLM_BASE_URL", "https://openrouter.ai/api/v1")

_CLIENT: Any = None


def _request_key(payload: dict) -> str:
    """A stable hash of everything that could change the answer."""
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:32]


def cache_path(local: bool = True) -> Path:
    """Where responses are read from and written to.

    Reads check the notebook's own ``artefacts/llm_cache/`` first, then the shared
    reference set. Writes only ever go to the local one — a lab must not edit the copy
    every other student depends on.
    """
    if local:
        return notebook_dir() / "artefacts" / "llm_cache"
    return solutions_cache_dir() / "llm_cache"


def _lookup(key: str) -> dict | None:
    for directory in (cache_path(local=True), cache_path(local=False)):
        candidate = directory / f"{key}.json"
        if candidate.exists():
            record = json.loads(candidate.read_text(encoding="utf-8"))
            record["cached"] = True
            return record
    return None


def _store(key: str, record: dict) -> None:
    directory = cache_path(local=True)
    directory.mkdir(parents=True, exist_ok=True)
    (directory / f"{key}.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8"
    )


def _client(base_url: str):
    global _CLIENT
    if _CLIENT is None:
        from openai import OpenAI

        from .env import require_key

        _CLIENT = OpenAI(api_key=require_key("OPENROUTER_API_KEY"), base_url=base_url)
    return _CLIENT


def _missing_key_error(prompt: str) -> RuntimeError:
    return RuntimeError(
        "\n"
        "No cached response for this prompt, and no API key to fetch one.\n"
        "لا توجد استجابة مخزَّنة لهذا الطلب، ولا مفتاح لجلب واحدة.\n"
        "\n"
        f"  prompt starts: {prompt.strip()[:90]!r}\n"
        "\n"
        "  Either put OPENROUTER_API_KEY in a .env file beside this notebook,\n"
        "  ضع OPENROUTER_API_KEY في ملف .env بجوار هذا الدفتر،\n"
        "  or re-run the cells above unchanged — the cache is keyed by the exact\n"
        "  أو أعد تشغيل الخلايا أعلاه كما هي، فالتخزين مرتبط بنصّ الطلب بالضبط،\n"
        "  prompt text, so an edited prompt is a new request.\n"
        "  فالطلب المُعدَّل طلبٌ جديد.\n"
    )


def chat(
    prompt: str,
    system: str | None = None,
    *,
    model: str | None = None,
    temperature: float = 0.0,
    max_tokens: int = 400,
    use_cache: bool = True,
    retries: int = 4,
) -> dict:
    """Send one prompt, return the answer and what it cost.

    Args:
        prompt: the user message.
        system: the system message, if any. Part of the cache key.
        model: slug to call. Defaults to :data:`DEFAULT_MODEL`.
        temperature: 0 by default, because a lab that measures needs the same answer twice.
        max_tokens: cap on the completion.
        use_cache: set False to force a live call. The response is still cached.
        retries: attempts on a rate-limited or transient failure, with backoff.

    Returns:
        ``{"text", "model", "cached", "latency_s", "prompt_tokens", "completion_tokens",
        "total_tokens"}``. ``latency_s`` is 0.0 on a cache hit, and ``cached`` says so —
        never average the two together and call it latency.

    Raises:
        RuntimeError: cache miss with no usable key, with an explanation of both.
    """
    model = model or DEFAULT_MODEL
    base_url = DEFAULT_BASE_URL
    payload = {"model": model, "system": system, "prompt": prompt,
               "temperature": temperature, "max_tokens": max_tokens}
    key = _request_key(payload)

    if use_cache:
        hit = _lookup(key)
        if hit is not None:
            return hit

    messages = ([{"role": "system", "content": system}] if system else [])
    messages.append({"role": "user", "content": prompt})

    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            started = time.perf_counter()
            response = _client(base_url).chat.completions.create(
                model=model, messages=messages,
                temperature=temperature, max_tokens=max_tokens,
            )
            latency = time.perf_counter() - started
            usage = getattr(response, "usage", None)
            record = {
                "text": (response.choices[0].message.content or "").strip(),
                "model": model,
                "cached": False,
                "latency_s": round(latency, 3),
                "prompt_tokens": getattr(usage, "prompt_tokens", None),
                "completion_tokens": getattr(usage, "completion_tokens", None),
                "total_tokens": getattr(usage, "total_tokens", None),
            }
            _store(key, record)
            return record
        except RuntimeError:
            # require_key failed: no key at all. A cache miss here is fatal and the
            # message has to say which of the two things is missing.
            raise _missing_key_error(prompt) from None
        except Exception as error:  # rate limit, timeout, transient 5xx
            last_error = error
            if attempt == retries - 1:
                break
            time.sleep(2 ** attempt)

    raise RuntimeError(
        f"The model call failed after {retries} attempts: {last_error}\n"
        f"فشل نداء النموذج بعد {retries} محاولات: {last_error}"
    ) from last_error


def cache_stats() -> dict:
    """How many responses each cache holds. Print it once; it explains a lot of confusion."""
    return {
        "local": len(list(cache_path(local=True).glob("*.json")))
        if cache_path(local=True).exists() else 0,
        "shared": len(list(cache_path(local=False).glob("*.json")))
        if cache_path(local=False).exists() else 0,
    }
