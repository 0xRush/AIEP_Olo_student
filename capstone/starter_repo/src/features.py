"""Build the feature table from the cleaned data.

Kept separate from data.py so that "what the data is" and "what the model sees" are two
different questions with two different answers. Week 3 day 2.
"""

from __future__ import annotations

import pandas as pd


def build_features(df: pd.DataFrame, target: str) -> tuple[pd.DataFrame, pd.Series]:
    """Return (X, y).

    Rules that matter:
      - The target must NOT appear in X. That is the classic leak.
      - No feature may use information unavailable at prediction time. A column filled
        in after the outcome is known will give you a wonderful score and a useless model.
      - Fitted transformations (scalers, encoders) do NOT belong here — they go in the
        pipeline in train.py, so they are fitted per fold and saved with the model.
    """
    df = df.copy()

    # TODO: engineer your features, with one line each on why it should carry signal.
    #   df["value_per_item"] = df["total"] / df["n_items"]   # captures basket size vs spend

    y = df[target]
    X = df.drop(columns=[target])

    # TODO: drop anything that leaks. Name each one and why.
    #   X = X.drop(columns=["settled_at"])   # only populated after the outcome is known

    assert target not in X.columns, "the target must not be inside X"
    return X, y
