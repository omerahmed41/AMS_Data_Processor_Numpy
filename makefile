
test:
	pytest --cov=. --cov-report html .

pylint:
	pylint *.py

setup:
	pip install -r requirements_dev.txt && pip install -r requirements.txt