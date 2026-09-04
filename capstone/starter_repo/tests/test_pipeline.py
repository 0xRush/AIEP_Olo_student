"""A few tests. Not required by the rubric, but they catch the failures that ruin a demo.

    make test
"""

from pathlib import Path

import pytest

from src.predict import load_model, predict


@pytest.fixture(scope="module")
def model_and_meta():
    if not Path("models/model.joblib").exists():
        pytest.skip("No trained model — run `make train` first.")
    return load_model()


def test_model_loads_in_a_fresh_process(model_and_meta):
    """Capstone requirement 3. This is the test a marker effectively runs by hand."""
    model, metadata = model_and_meta
    assert model is not None
    assert metadata.get("features"), "metadata must record the feature list"


def test_predict_returns_a_label(model_and_meta):
    model, metadata = model_and_meta
    # TODO: a real example record.
    result = predict({}, model, metadata)
    assert "label" in result


def test_missing_field_raises_a_clear_error(model_and_meta):
    """Bad input must fail with a message, not a KeyError from deep inside sklearn."""
    model, metadata = model_and_meta
    with pytest.raises(ValueError):
        predict({"definitely_not_a_real_field": 1}, model, metadata)
