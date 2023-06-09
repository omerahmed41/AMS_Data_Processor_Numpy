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

