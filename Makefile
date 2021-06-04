test:
	PYTHONPATH=. pytest --cov=runflow --cov-report=term --cov-report=html tests
