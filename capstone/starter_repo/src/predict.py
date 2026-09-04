"""Load the artifact and predict. The ONLY sanctioned inference path.

Capstone requirement 3. Everything — the API, the Streamlit page, a colleague's script —
calls this. One inference path means training and serving cannot drift apart, which is
the failure taught in week 6 day 3.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd

MODEL_DIR = Path("models")


def load_model(model_dir: Path = MODEL_DIR):
    """Load the fitted pipeline and its metadata. Works in a fresh process."""
    model_path = model_dir / "model.joblib"
    meta_path = model_dir / "metadata.json"

    if not model_path.exists():
        raise FileNotFoundError(
            f"No model at {model_path}. Run `make train` first."
        )

    model = joblib.load(model_path)
    metadata = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    return model, metadata


def predict(payload: dict[str, Any] | pd.DataFrame, model=None, metadata=None) -> dict[str, Any]:
    """Predict for one record (a dict) or several (a DataFrame).

    Returns the label and a confidence. Returning a confidence is not decoration: the
    caller cannot tell a certain answer from a guess without it.
    """
    if model is None:
        model, metadata = load_model()
    metadata = metadata or {}

    frame = payload if isinstance(payload, pd.DataFrame) else pd.DataFrame([payload])

    expected = metadata.get("features")
    if expected:
        missing = [c for c in expected if c not in frame.columns]
        if missing:
            raise ValueError(f"Missing required field(s): {missing}")
        frame = frame[expected]

    label = model.predict(frame)[0]

    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = float(model.predict_proba(frame).max())

    # TODO: pick a threshold from your validation data, not from thin air.
    # An input unlike anything in training should return "unknown", not a wrong label.
    THRESHOLD = 0.0
    if confidence is not None and confidence < THRESHOLD:
        return {"label": "unknown", "confidence": confidence}

    return {"label": label if isinstance(label, str) else label.item(), "confidence": confidence}


if __name__ == "__main__":
    loaded_model, loaded_meta = load_model()
    print("Loaded model trained on", loaded_meta.get("trained_on", "(unknown date)"))
    # TODO: put a real example record here so this file doubles as a smoke test.
    print(predict({}, loaded_model, loaded_meta))
