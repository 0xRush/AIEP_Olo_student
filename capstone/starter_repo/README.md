# <Your Project Name>

<One sentence: what this predicts or retrieves, and who would use it.>

<div dir="rtl" align="right">

# <اسم مشروعك>

<جملة واحدة: بماذا يتنبّأ هذا النظام أو ماذا يسترجع، ومن يستخدمه.>

</div>

---

> **This is the capstone starter skeleton.** Copy it, rename it, and replace every `<...>` and every
> `TODO`. Delete this block when you do.
>
> A marker will clone this repository into an empty directory and follow this README literally. If they
> get stuck, that costs you marks under criterion 5 of `capstone/rubric.md`. Test it yourself from a
> clean clone before demo day.

## Quickstart

```bash
git clone <your-repo-url>
cd <your-repo>
uv venv && source .venv/bin/activate       # or reuse the course env: conda activate aiep
uv pip install -r requirements.txt

make data      # download / pull the raw data
make train     # rebuild the model from raw data  ← capstone requirement 2
make serve     # start the API on http://localhost:8000
```

Then send it something:

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"<field>": <value>}'
```

## What this does

<Two or three sentences. What problem, what data, what the output means.>

## Results

| Model | <your metric> | Notes |
|---|---|---|
| Baseline (<what it is>) | 0.00 | <why this is the right dumb baseline> |
| <your model> | 0.00 | |

Full write-up: `report.pdf` — **add yours here** (this link is dead until you do)

## Data

| | |
|---|---|
| Source | <url> |
| Licence | <licence> |
| Rows / items | <n> |
| Obtained | <date, and how — API, scrape, download> |
| Known problem | <the thing that is wrong with it> |

Raw data is **not** committed. `make data` reproduces it.

## Project layout

```
src/
  data.py       load and clean the raw data
  features.py   build the feature table
  train.py      train, evaluate, and save the artifact
  predict.py    load the artifact and predict — the ONLY sanctioned inference path
app/
  main.py       FastAPI service
  ui.py         Streamlit demo page (optional)
models/         the saved artifact (gitignored except metadata)
notebooks/      exploration only — the pipeline does not live here
report.md       the technical report
```

## Requirements

Python 3.11. See `requirements.txt`.

## AI assistance

See [`AI_USAGE.md`](AI_USAGE.md) — delete this section if you did not use any beyond documentation
and debugging.
