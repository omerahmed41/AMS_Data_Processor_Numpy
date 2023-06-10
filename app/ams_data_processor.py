"""
This module provides functionality for processing AMS files.

"""
from domain.ams_processor import AMSProcessor
from domain.data_modifier import DataModifier
from domain import io_handler
from domain.operations import OperationFactory


def main(file_path, formula, output_dir):
    """
        Entry point of the AMS data processor script.

        This function reads the input file, processes the data, and generates output files.
        """
    try:
        content = io_handler.read_file(file_path)

        ams_processor = AMSProcessor(content)
        analyses_data = ams_processor.extract_analyses_data()
        header, analysis_array = ams_processor.parse_analyses_data(analyses_data)

        operation = OperationFactory().create(formula)
        data_modifier = DataModifier(operation)
        modified_data = data_modifier.modify(analysis_array)

        io_handler.print_to_html(output_dir, analysis_array, modified_data, header)

    except FileNotFoundError as file_not_found_error:
        print(f"FileNotFoundError: {str(file_not_found_error)}")

    except ValueError as value_error:
        print(f"ValueError: {str(value_error)}")
