from unittest.mock import patch, mock_open
import pytest

from infrastructure.file_reader_factory import AMSFileReader, FileReaderFactory


def test_ams_file_reader(mock_file_content):
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        file_reader = AMSFileReader("dummy_file_path")
        content = file_reader.read()
        assert content == mock_file_content


def test_file_reader_factory(mock_file_content):
    file_reader = FileReaderFactory.create("dummy_file_path")
    assert isinstance(file_reader, AMSFileReader)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        file_reader = AMSFileReader("non_existent_file_path")
        file_reader.read()

