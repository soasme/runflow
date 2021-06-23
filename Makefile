test:
	PYTHONPATH=. python3 -mpytest --cov=runflow --cov-report=term --cov-report=html tests

lint:
	python3 -mflake8 runflow
	python3 -mpylint runflow
