# AMS Data Processor

The AMS Data Processor is a Python script that allows you to process AMS measurement files by applying mathematical formulas to the data. It extracts analysis records from the file, performs specified mathematical operations, and generates HTML output files with the modified data.

## Features

- Reads AMS measurement files and extracts analysis records.
- Applies various mathematical formulas to the data, including sum, division, multiplication, square root, subtraction, and natural logarithm.
- Generates HTML output files with the modified data in a tabular format.

## Setup
To set up the project, run `make setup`.

## Pylint
To run Pylint for code analysis, use `make pylint`.

## Run All Tests with Coverage
To run all tests with a coverage report, use `make test`.

## Run Pre-commit Hooks
To run pre-commit hooks, including Pylint and other linting tools, use `pre-commit run --all-files`.

## Jenkins CI/CD Pipeline
I have included a sample Jenkinsfile that can be used for the pipeline on platforms like Bitbucket.

## Usage

To run the AMS Data Processor, use the following command-line syntax:

`ams_data_processor.py inputs/C14_setting.ams sum output`

Please note that the above command assumes the script name is `ams_data_processor.py`, and the input file is located in the provided path.

## Technology Stack & Features:
* Pandas
* NumPy
* cProfile
* Dependency graph
* Pylint
* Pre-commit
* Test coverage report
* Docker with Docker Compose
* Makefile
* Logs
* Jenkins CI/CD Pipeline
* Kubernetes
* Design patterns (Pub-Sub, Command, Repository, Singleton)
* Layer architecture (DDD)
* Sphinx documentation

## DDD and Layer Architecture 
I followed the Domain Driven Design with the Layer architecture.
To see the Architecture graph, run `make profile-graph-cluster`.

![profile_graph_cluster](https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/77e7498e-05fd-4d78-8e5f-e95b0098ce55)


## Full Dependency Graph:
To see the full dependency graph, run `make profile-graph`.

![ams_data_processor](https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/ecff1848-9636-4e7c-b915-ca8f935afc79)

## Call-graph to Improve Performance 
If you want to see which parts of the code are taking the most time (the bottleneck), run `make profile`. 

![Screenshot 2023-06-10 at 12 15 30 PM](https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/30dc8de3-1a56-40f5-84e1-43dff827b0be)

Here we see that writing data takes more than 80% of the run time, which may be a good place to start refactoring.

## Test Coverage:
To run all tests and see the test coverage report, run `make test`.

![Screenshot 2023-06-10 at 12 18 08 PM](https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/9cf06a03-3058-497d-92f7-3a5bf4752b2a)

## Documentations:
Run `make documentations` to create documentation for the project.
