test:
	PYTHONPATH=. python3 -mpytest --cov=runflow --cov-report=term --cov-report=html tests

style:
	python3 -mblack --line-length 79 runflow

lint:
	python3 -mflake8 runflow
	python3 -mpylint runflow
