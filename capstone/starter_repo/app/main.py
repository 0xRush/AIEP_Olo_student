"""FastAPI service — capstone requirement 4.

    make serve       # then open http://localhost:8000/docs

Two things this file gets right that most student services get wrong:

  1. The model is loaded ONCE at startup, not per request.
  2. Bad input returns a readable error, not a stack trace.

Replace every TODO.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.predict import load_model, predict

# Loaded at startup, held for the process lifetime. Loading inside the request handler
# makes every request take seconds instead of milliseconds.
STATE: dict[str, Any] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        STATE["model"], STATE["metadata"] = load_model()
        print("Model loaded:", STATE["metadata"].get("trained_on", "(unknown date)"))
    except FileNotFoundError as exc:
        # Start anyway so /health can report the problem, rather than crashing silently.
        print(f"WARNING: {exc}")
        STATE["model"], STATE["metadata"] = None, {}
    yield
    STATE.clear()


app = FastAPI(title="<Your Project>", version="1.0.0", lifespan=lifespan)


class PredictRequest(BaseModel):
    """TODO: replace these with your actual input fields.

    Pydantic validates them for you — use Field constraints so bad input is rejected
    before it reaches the model.
    """

    # example_numeric: float = Field(..., ge=0, description="must not be negative")
    # example_category: str = Field(..., max_length=64)
    pass


class PredictResponse(BaseModel):
    label: str
    confidence: float | None = None


@app.get("/health")
def health() -> dict[str, Any]:
    """Is the service up, and is a model actually loaded?"""
    return {
        "status": "ok" if STATE.get("model") is not None else "no model loaded",
        "model_trained_on": STATE.get("metadata", {}).get("trained_on"),
    }


@app.post("/predict", response_model=PredictResponse)
def predict_endpoint(request: PredictRequest) -> PredictResponse:
    if STATE.get("model") is None:
        raise HTTPException(status_code=503, detail="No model loaded. Run `make train` first.")

    try:
        result = predict(request.model_dump(), STATE["model"], STATE["metadata"])
    except ValueError as exc:
        # The caller sent something wrong — say what, clearly.
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        # Never leak an internal traceback to the caller. Log it, return something safe.
        print(f"ERROR during prediction: {exc}")
        raise HTTPException(status_code=500, detail="Prediction failed.") from exc

    return PredictResponse(**result)


# --- For an image or file model, use this shape instead ---------------------------
#
# from fastapi import File, UploadFile
#
# MAX_BYTES = 5 * 1024 * 1024
#
# @app.post("/predict-image", response_model=PredictResponse)
# async def predict_image(file: UploadFile = File(...)) -> PredictResponse:
#     if not (file.content_type or "").startswith("image/"):
#         raise HTTPException(status_code=400, detail="Expected an image file.")
#     data = await file.read()
#     if len(data) > MAX_BYTES:
#         raise HTTPException(status_code=413, detail="File too large (max 5 MB).")
#     ...
