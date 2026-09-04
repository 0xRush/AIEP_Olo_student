"""Streamlit demo page — optional, and excellent for demo day.

    make ui

Not a production frontend. Its job is to make five minutes on demo day convincing, and
it does that better than a terminal full of curl commands.
"""

from __future__ import annotations

import streamlit as st

from src.predict import load_model, predict

st.set_page_config(page_title="<Your Project>", page_icon="🔮")

st.title("<Your Project>")
st.caption("<One sentence: what this predicts and who it is for.>")


@st.cache_resource
def get_model():
    """Cached so the model loads once per session, not once per interaction."""
    return load_model()


try:
    model, metadata = get_model()
except FileNotFoundError as exc:
    st.error(f"{exc}")
    st.stop()

with st.sidebar:
    st.subheader("Model")
    st.write("Trained:", metadata.get("trained_on", "unknown"))
    st.write("Baseline:", metadata.get("baseline", {}))
    st.write("Model:", metadata.get("metrics", {}))

# TODO: replace with your actual inputs.
st.subheader("Input")
payload = {}
# payload["example_numeric"] = st.number_input("Example numeric", min_value=0.0)
# payload["example_category"] = st.selectbox("Example category", ["a", "b", "c"])

if st.button("Predict", type="primary"):
    try:
        result = predict(payload, model, metadata)
    except ValueError as exc:
        st.error(str(exc))
    else:
        st.subheader("Result")
        st.metric("Prediction", result["label"])
        if result.get("confidence") is not None:
            st.progress(result["confidence"], text=f"Confidence: {result['confidence']:.1%}")
            if result["label"] == "unknown":
                st.warning("Confidence is below the threshold — this input looks unlike the training data.")
