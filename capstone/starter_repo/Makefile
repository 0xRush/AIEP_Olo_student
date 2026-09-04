.PHONY: help data train serve ui test clean

help:
	@echo "make data    - fetch / rebuild the raw dataset"
	@echo "make train   - train the model from raw data and save the artifact"
	@echo "make serve   - start the prediction API"
	@echo "make ui      - start the Streamlit demo"
	@echo "make test    - run the tests"

data:
	python -m src.data

# Capstone requirement 2: ONE command rebuilds the model from raw data.
train:
	python -m src.train

serve:
	uvicorn app.main:app --reload --port 8000

ui:
	streamlit run app/ui.py

test:
	pytest -q

clean:
	rm -rf models/*.joblib models/*.pt __pycache__ .pytest_cache
