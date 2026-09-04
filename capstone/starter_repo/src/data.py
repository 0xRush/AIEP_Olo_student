"""Load and clean the raw data.

Capstone requirement 2: this must be reproducible. `make data` runs it, and running it
twice must produce the same output.

Replace every TODO. Delete the parts you do not need.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def fetch_raw() -> Path:
    """Obtain the raw data and return the path to it.

    Whatever this does — call an API, download a file, read a scrape — it must be
    repeatable. A marker will run it on a clean machine.

    If the source is rate-limited or slow, cache to RAW_DIR and skip the fetch when the
    file already exists. Say so in the README.
    """
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    target = RAW_DIR / "raw.csv"

    if target.exists():
        print(f"Using cached raw data at {target}")
        return target

    # TODO: fetch the data. For example:
    #   response = requests.get(URL, timeout=60); target.write_bytes(response.content)
    raise NotImplementedError("Implement fetch_raw()")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the raw frame.

    Write down WHY for each decision, not just what — the report needs it, and so does
    anyone reading this in three weeks. One comment per decision is enough.
    """
    df = df.copy()

    # TODO: drop duplicates, fix dtypes, handle missing values, normalise categories.
    # Each with a one-line reason:
    #   df = df.drop_duplicates()                       # same order logged twice by the API
    #   df["total"] = pd.to_numeric(df["total"], "coerce")  # stored as text, blank for new rows

    return df


def load() -> pd.DataFrame:
    """Fetch, clean, cache, and return the processed data.

    This is the function everything else imports. Nothing else should read from
    data/raw directly.
    """
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    cached = PROCESSED_DIR / "clean.parquet"

    if cached.exists():
        return pd.read_parquet(cached)

    raw_path = fetch_raw()
    df = clean(pd.read_csv(raw_path))
    df.to_parquet(cached, index=False)
    print(f"Wrote {cached}  ({len(df):,} rows)")
    return df


if __name__ == "__main__":
    frame = load()
    print(frame.shape)
    print(frame.head())
