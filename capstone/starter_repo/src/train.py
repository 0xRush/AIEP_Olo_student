"""Train, evaluate, and save the model artifact.

`make train` runs this. Capstone requirements 2, 3, and 5 all land here:

  2. It rebuilds the model from raw data in one command.
  3. It saves weights AND the fitted preprocessing, plus metadata.
  5. It compares against a baseline and reports an honest metric.

Replace every TODO.
"""

from __future__ import annotations

import json
import platform
import sys
from datetime import date
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier  # or DummyRegressor
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from src.data import load
from src.features import build_features

MODEL_DIR = Path("models")
SEED = 42

# TODO: name your target column.
TARGET = "<target_column>"


def build_pipeline() -> Pipeline:
    """Return the full pipeline: preprocessing AND the estimator.

    Everything fitted goes INSIDE. That is what makes the saved artifact loadable in a
    fresh process, and it is what stops preprocessing leaking across the split.
    See week 3 day 4.
    """
    # TODO: build it, e.g.
    #   ColumnTransformer(...) -> StandardScaler / OneHotEncoder -> your estimator
    raise NotImplementedError("Implement build_pipeline()")


def evaluate(y_true, y_pred) -> dict[str, float]:
    """Compute the metrics that matter for THIS problem.

    Accuracy on imbalanced data is not a metric, it is a way of not looking. Pick what
    fits the problem and justify it in the report.
    """
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1": float(f1_score(y_true, y_pred, average="weighted")),
        # TODO: add the metric you actually chose, and remove any of these that mislead.
    }


def main() -> None:
    df = load()
    X, y = build_features(df, target=TARGET)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED,
        # TODO: stratify=y for classification. For time series, split by TIME, not randomly.
    )

    # --- The baseline. Deliberately dumb. Requirement 5. -------------------------
    baseline = DummyClassifier(strategy="most_frequent", random_state=SEED)
    baseline.fit(X_train, y_train)
    baseline_metrics = evaluate(y_test, baseline.predict(X_test))
    print(f"Baseline : {baseline_metrics}")

    # --- The real model ----------------------------------------------------------
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)
    model_metrics = evaluate(y_test, pipeline.predict(X_test))
    print(f"Model    : {model_metrics}")

    # --- Save the artifact. Requirement 3. --------------------------------------
    # joblib.dump on the WHOLE pipeline — the fitted scaler and encoder are part of the
    # model. Saving the estimator alone produces an artifact nobody can use.
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_DIR / "model.joblib")

    metadata = {
        "target": TARGET,
        "features": list(X.columns),
        "classes": sorted(pd.Series(y).unique().tolist()),
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
        "baseline": baseline_metrics,
        "metrics": model_metrics,
        "seed": SEED,
        "trained_on": date.today().isoformat(),
        "python": platform.python_version(),
        "sklearn": __import__("sklearn").__version__,
    }
    (MODEL_DIR / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(f"\nSaved {MODEL_DIR / 'model.joblib'} and metadata.json")

    if model_metrics["f1"] <= baseline_metrics["f1"]:
        print("\n⚠️  Your model does not beat the baseline. That is a finding — report it "
              "honestly rather than tuning until the number looks better.", file=sys.stderr)


if __name__ == "__main__":
    main()
