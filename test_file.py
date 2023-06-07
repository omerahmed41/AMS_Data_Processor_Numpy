import pytest
import os
from unittest.mock import patch, mock_open
from ams_data_processor import AMSProcessor, AMSFileReader, FileReaderFactory, OperationFactory, DataModifier, \
    OutputWriter

# Mocking file content for AMSFileReader
mock_file_content = "# Analyses\n1\t2\t3\n4\t5\t6\n#"

# Testing AMSFileReader
def test_ams_file_reader():
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        file_reader = AMSFileReader("dummy_file_path")
        content = file_reader.read()
        assert content == mock_file_content

# Testing FileReaderFactory
def test_file_reader_factory():
    file_reader = FileReaderFactory.create("dummy_file_path")
    assert isinstance(file_reader, AMSFileReader)

# Testing AMSProcessor
def test_ams_processor():
    ams_processor = AMSProcessor(mock_file_content)
    analyses_data = ams_processor.extract_analyses_data()
    assert analyses_data == ['1\t2\t3', '4\t5\t6']
    header, analysis_array = ams_processor.parse_analyses_data(analyses_data)
    assert (header == ['1', '2', '3']).all()
    assert (analysis_array == [['4', '5', '6']]).all()

# Testing OperationFactory
def test_operation_factory():
    operation = OperationFactory().create("sum").apply
    assert operation(5) == "++5.05++"
    with pytest.raises(ValueError):
        operation = OperationFactory().create("unsupported_operation")

# Testing DataModifier
def test_data_modifier():
    operation = OperationFactory().create("sum")
    data_modifier = DataModifier(operation)
    analysis_array = [['1', '2', '3'], ['4', '5', '6']]
    modified_array = data_modifier.modify(analysis_array)
    assert (modified_array == [['++1.01++', '++2.02++', '++3.03++'], ['4', '5', '6']]).all()

# Testing edge cases for OperationFactory
def test_operation_factory_edge_cases():
    operation = OperationFactory().create("Division").apply
    assert operation(0) == 0  # Division by zero
    assert operation(-1) == "//-1.0//"  # Division by a negative number
    assert operation('inf') == 'inf'  # Division by infinity
    # assert operation(float('inf')) == 'inf'  # Division by infinity

    operation = OperationFactory().create("Natural logarithm").apply
    assert operation(0) == 0  # Logarithm of zero
    assert operation(1) == '..0.0..'  # Logarithm of one
    assert operation(float('inf')) == '..inf..'  # Logarithm of infinity


# Testing when the file does not exist
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        file_reader = AMSFileReader("non_existent_file_path")
        file_reader.read()


# Testing the output writer
def test_output_writer():
    output_file = "./output/file_name.html"
    output_writer = OutputWriter("output")
    output_writer.write_html_table(["dummy_data"], ["dummy_header"], "file_name.html")
    assert os.path.exists(output_file)


# Testing for invalid formulas
def test_invalid_formula():
    with pytest.raises(ValueError):
        operation = OperationFactory().create("invalid_formula")


