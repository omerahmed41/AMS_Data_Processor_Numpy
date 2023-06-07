
test:
	pytest --cov=. --cov-report html .

pylint:
	pytest --cov=. --cov-report html .

setup:
	pip install -r requirements_dev.txt && pip install -r requirements.txt