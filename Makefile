test:
	PYTHONPATH=. python3 -mpytest --cov=runflow --cov-report=term --cov-report=html tests

style:
	python3 -mblack --line-length 79 --exclude runflow/hcl2_parser.py runflow

lint:
	python3 -mflake8 runflow
	python3 -mpylint runflow

hcl2:
	python3 -mlark.tools.standalone runflow/hcl2.lark -s eval -s module > runflow/hcl2_parser.py
