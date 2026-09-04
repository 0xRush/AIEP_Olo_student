# shared/

Course-wide infrastructure every lab relies on. Lab authors read this; students normally don't need
to open it.

<div dir="rtl" align="right">

# مجلّد shared

البنية التحتية المشتركة التي يعتمد عليها كل معمل. يقرؤه مؤلّفو المعامل، ولا يحتاج الطلاب عادةً لفتحه.

</div>

---

## Contents

| Asset | Purpose |
|---|---|
| `aiep/` | The helper package every notebook imports. Installed with `pip install -e shared/` |
| `pyproject.toml` | Makes `aiep` installable — including straight from a URL on Colab |
| `datasets.yaml` | The dataset registry. Every dataset is declared here before its lab is written |
| `data_cache/` | Small committed fixtures. Larger files download from Releases into here |
| `solutions_cache/` | Reference artefacts, so a student who missed a day isn't blocked tomorrow |
| `notebook_template.ipynb` | Start every new lab from this, not from a blank notebook |

## The `aiep` package

Deliberately tiny — its only hard dependencies are `pyyaml` and `requests`, so it installs on Colab in
about a second. Everything heavy (torch, sklearn, transformers) is a *lab* dependency, installed by
`environment.yml` locally or by the notebook's `ensure(...)` call on Colab.

| Module | What it does |
|---|---|
| `aiep.paths` | Finds the repo root, the data cache, and the lab's `artefacts/` — on a laptop, on Windows, or on Colab where no checkout exists |
| `aiep.data` | `get_dataset(name)` and `load_artefact(name)`. This is why no notebook contains a file path |
| `aiep.env` | `ensure(*pkgs)`, `seed_everything()`, `device()`, `require_key()` |
| `aiep.checks` | `check(cond, en, ar)` and `report()` — bilingual sanity checks |
| `aiep.viz` | Course-wide plot style, confusion matrix, training curves, image grids |

### The four lines every lab uses

```python
from aiep.env import ensure, seed_everything, device
from aiep.data import get_dataset
from aiep.paths import ARTEFACT_DIR
from aiep.checks import check, report
```

## Local setup

```bash
conda env create -f ../environment.yml
conda activate aiep
uv pip install -r ../requirements.lock
pip install -e .            # from inside shared/
```

Or from the repo root: `make setup`, which also registers the Jupyter kernel and fetches the datasets.

## On Colab

Nothing here needs to be on disk first. The notebook's portable setup cell installs `aiep` from the
student repo by URL, and `get_dataset()` downloads what the lab needs into the session. See
[`../docs/Data_Guide.md`](../docs/Data_Guide.md).

## Adding to it

- **A new dataset** → register it in `datasets.yaml` with all required fields, then
  `python ../tools/fetch_datasets.py --update-hashes`. Rules in
  [`../docs/Data_Guide.md`](../docs/Data_Guide.md).
- **A helper used by two or more labs** → add it to the right `aiep` module. A helper used by exactly
  one lab belongs in that lab's notebook, where students can read it.
- **A reference artefact** → drop it in `solutions_cache/` and make sure the consuming lab calls
  `load_artefact()` rather than a bare path.

Keep `aiep` small. It exists to remove environment friction, not to hide the machine learning — if a
student would learn something by writing a function themselves, it does not belong here.
