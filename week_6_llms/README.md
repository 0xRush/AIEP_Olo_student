# Week 6 — LLMs

Last week you ran a small language model and read its next-token probabilities. This
week we take that primitive and build on top: measure where modern LLMs cost you
(tokens, perplexity, decoding), ground them in your own documents with RAG, give
them tools and let them act as agents, and finally compress and fine-tune them so
they fit on free Colab hardware.

<div dir="rtl" align="right">

# الأسبوع السادس — النماذج اللغوية الكبيرة

في الأسبوع الماضي شغّلت نموذجًا لغويًّا صغيرًا وقرأت احتمالات رمزه التالي. هذا
الأسبوع نأخذ هذه الأساسيّات ونبني فوقها: نقيس تكلفة النماذج الحديثة (الرموز، الحيرة،
فكّ الترميز)، نُلحقها بوثائقك عبر RAG، نعطيها أدوات ونجعلها تعمل كوكلاء، وأخيرًا
نضغطها ونضبطها لتسع على موارد Colab المجانية.

</div>

---

## What you'll be able to do by the end of the week

- Measure how a GPT-2-scale model sees Arabic vs English — in tokens AND in
  perplexity — and explain the cost of using the wrong-language model.
- Find the single most surprising token in a sentence under a given model.
- Tune decoding (greedy, temperature, top-k, top-p) for two different tasks.
- Build a Retrieval-Augmented Generation (RAG) pipeline from scratch: chunk a
  corpus, embed it, retrieve the top-k relevant chunks, and ground an LLM answer
  in them. Compare with-RAG vs no-RAG on the same question.
- Build a tool-calling agent that uses the ReAct loop (Reason → Act → Observe →
  Repeat) and completes a multi-step task a plain LLM cannot.
- Fine-tune a small LLM with LoRA on a specific task, then run it with 4-bit
  quantization, and measure the memory + latency delta.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تقيس كيف يرى نموذج بحجم GPT-2 العربيّةَ مقابل الإنجليزيّة — بالرموز وبالحيرة —
  وتشرح تكلفة استخدام نموذج بلغة خاطئة.
- أن تجد الرمز الأكثر مفاجأةً في جملة تحت نموذج معيّن.
- أن تضبط فكّ الترميز (greedy, temperature, top-k, top-p) لمهمّتين مختلفتين.
- أن تبني خطّ RAG من الصفر: تجزئة، تضمين، استرجاع أعلى k مقطع، وربط إجابة LLM بها.
  قارن مع-RAG وبدون-RAG على نفس السؤال.
- أن تبني وكيلًا باستدعاء أدوات بأسلوب ReAct (استدلال → فعل → ملاحظة → تكرار).
- أن تضبط نموذجًا صغيرًا بـLoRA على مهمّة محدّدة، ثم تُشغّله بتكميم ٤-بت وتقيس فرق
  الذاكرة والزمن.

</div>

---

## Days

| Day | Theme | Lab |
|-----|-------|-----|
| D1 | Language Modeling: Tokens, Perplexity, Decoding | `D1_lm_perplexity` |
| D2 | Modern LLMs & RAG | `D2_rag_llm` |
| D3 | Agentic AI: Tools, ReAct, Memory | `D3_agents` |
| D4 | Efficient LLM Adaptation: LoRA + Quantization | `D4_lora_quant` |
| D5 | Kaggle competition OR VLMs (TBD) | TBD |

Each lab ships three notebooks: `*_solution.ipynb` (instructor), `*_blank.ipynb` and
`*_guided.ipynb` (student). Variants are generated with `tools/make_variants.py`.
