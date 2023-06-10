
test:
	pytest --cov=. --cov-report html .

pylint:
	pylint *.py

setup:
	pip install -r requirements_dev.txt && pip install -r requirements.txt

profile:
	python profiler.py  /Users/omerSuliman/Downloads/ams_data_processor/inputs/c14.ams  sum  output

profile-graph:
	pydeps ams_data_processor.py --max-bacon 3 --reverse -v

profile-graph-cluster:
	pydeps ams_data_processor.py --max-bacon 3 --reverse --cluster -o profile_graph_cluster.svg