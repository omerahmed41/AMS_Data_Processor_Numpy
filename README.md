# AMS Data Processor

The AMS Data Processor is a Python script that allows you to process AMS measurement files by applying mathematical formulas to the data. It extracts analysis records from the file, performs specified mathematical operations, and generates HTML output files with the modified data.

## Features

- Read AMS measurement files and extract analysis records.
- Apply various mathematical formulas to the data, including sum, division, multiplication, square root, subtraction, and natural logarithm.
- Generate HTML output files with the modified data in a tabular format.

## setup
run `make setup`

## pylint
run `make pylint`

## run all test with --cov
run `make test`

## run pre-commit with pylint and all  lints libs.
run `pre-commit run --all-files`


## Jenkins CI/CD pipline
I added sample jenkins file to use it for pipline on Bitbuket for example.
## Usage

To run the AMS Data Processor, use the following command-line syntax:
`ams_data_processor.py inputs/C14_setting.ams sum  output`