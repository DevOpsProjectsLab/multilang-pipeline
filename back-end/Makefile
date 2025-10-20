.PHONY: run test unit integration

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest

unit:
	pytest tests/unit -q

integration:
	pytest tests/integration -q
