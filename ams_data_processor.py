import os
import re
import math
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod


class IOperation:
    def apply(self, value):
        if value in ['nan', 'inf']:
            return value
        try:
            return self.perform_operation(float(value))
        except:
            return value

    def perform_operation(self, value):
        raise NotImplementedError

class SumOperation(IOperation):
    def perform_operation(self, value):
        return f"++{value + (0.01 * value)}++"

class DivisionOperation(IOperation):
    def perform_operation(self, value):
        return f"//{1 / value}//"

class MultiplicationOperation(IOperation):
    def perform_operation(self, value):
        return f"**{value * value * 0.2}**"

class SquareRootOperation(IOperation):
    def perform_operation(self, value):
        return f"##{math.sqrt(value)}##"

class SubtractionOperation(IOperation):
    def perform_operation(self, value):
        return f"--{value - (0.01 * value)}--"

class NaturalLogarithmOperation(IOperation):
    def perform_operation(self, value):
        return f"..{math.log(value)}.."


class IFileReader(ABC):
    @abstractmethod
    def read(self):
        pass


class AMSFileReader(IFileReader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def read(self):
        with open(self.file_path, 'r') as file:
            self.content = file.read()
        return self.content


class FileReaderFactory:
    @staticmethod
    def create(file_path):
        # Add conditions here to support more file formats
        return AMSFileReader(file_path)


class AMSProcessor:
    def __init__(self, content):
        self.content = content

    def extract_analyses_data(self):
        analyses_section = re.search(r'# Analyses(.*?)#', self.content, re.DOTALL)
        if analyses_section is None:
            raise ValueError("No analysis records found in the 'analyses' section.")
        analyses_data = analyses_section.group(1).strip().split('\n')

        if not analyses_data:
            raise ValueError("No analysis records found in the 'analyses' section.")
        analyses_data = analyses_data[:5]
        return analyses_data

    def parse_analyses_data(self, analyses_data):
        # Convert to dictionary
        analysis_array = np.array([row.split('\t') for row in analyses_data])

        # Remove the header row
        header = analysis_array[0]
        analysis_array = analysis_array[1:]

        return header, analysis_array


class OperationFactory:
    def create(self, operation):
        if operation.lower() == "sum":
            return SumOperation()
        elif operation.lower() == "division":
            return DivisionOperation()
        elif operation.lower() == "multiplication":
            return MultiplicationOperation()
        elif operation.lower() == "square root":
            return SquareRootOperation()
        elif operation.lower() == "subtraction":
            return SubtractionOperation()
        elif operation.lower() == "natural logarithm":
            return NaturalLogarithmOperation()
        else:
            raise ValueError("Invalid operation")


class DataModifier:
    def __init__(self, operation):
        self.operation = operation

    def modify(self, analysis_array):
        df = pd.DataFrame(analysis_array)
        df.iloc[::2] = df.iloc[::2].applymap(self.operation.apply)
        return df.to_numpy()


class OutputWriter:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def write_html_table(self, analysis_array, header, output_filename):
        df = pd.DataFrame(analysis_array, columns=header)
        html = df.to_html()

        output_file_path = os.path.join(self.output_dir, output_filename)
        with open(output_file_path, "w") as file:
            file.write(html)
        print(f"Results have been written to {output_file_path}.")


def main(file_path, formula, output_dir):
    file_reader = FileReaderFactory.create(file_path)
    content = file_reader.read()

    ams_processor = AMSProcessor(content)
    analyses_data = ams_processor.extract_analyses_data()
    header, analysis_array = ams_processor.parse_analyses_data(analyses_data)

    # Get operation and modify data
    operation = OperationFactory().create(formula)
    data_modifier = DataModifier(operation)
    modified_data = data_modifier.modify(analysis_array)

    output_writer = OutputWriter(output_dir)
    output_writer.write_html_table(analysis_array, header, 'analyses_table_old_data.html')
    output_writer.write_html_table(modified_data, header, 'analyses_table_updated_data.html')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='AMS file processing')
    parser.add_argument('file_path', type=str, help='Path to the AMS measurement file')
    parser.add_argument('formula', type=str, help='Mathematical formula to be applied')
    parser.add_argument('output_dir', type=str, help='Directory to store the output files')
    args = parser.parse_args()

    main(args.file_path, args.formula, args.output_dir)
