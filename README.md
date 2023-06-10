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
To run all tests with coverage report, use `make test`.

## Run Pre-commit Hooks
To run pre-commit hooks, including Pylint and other linting tools, use `pre-commit run --all-files`.

## Jenkins CI/CD Pipeline
I have included a sample Jenkinsfile that can be used for the pipeline on platforms like Bitbucket.

## Usage

To run the AMS Data Processor, use the following command-line syntax:

`ams_data_processor.py inputs/C14_setting.ams sum  output`


Please note that the above command assumes the script name is `ams_data_processor.py`, the input file is located in the provided path.

## DDD and Layer Architecture 
I followed the Domain Driven Design with the Layer archtitcaure, run `make profile-graph-cluster`to see the Architecture grapg
![profile_graph_cluster](https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/77e7498e-05fd-4d78-8e5f-e95b0098ce55)


Full dependency Graph:
see the full dependency Graph run `make profile-graph`
![ams_data_processor](https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/ecff1848-9636-4e7c-b915-ca8f935afc79)

#Call graph- Improve performance 
if you want to see which parts of the code that taking the most time (The bottleneck) run `make profile` 
<img width="1440" alt="Screenshot 2023-06-10 at 12 15 30 PM" src="https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/30dc8de3-1a56-40f5-84e1-43dff827b0be">

* he we see writing Data take more than 80% of the run time, mebe a good place to start refactoring.

Test Coverage:
to run all tests and see test coverage report run `make test`
<img width="1440" alt="Screenshot 2023-06-10 at 12 18 08 PM" src="https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/9cf06a03-3058-497d-92f7-3a5bf4752b2a">

