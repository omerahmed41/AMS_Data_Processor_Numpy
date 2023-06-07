"""
Integration tests for the AMS data processor module.

"""
import os
from unittest.mock import patch
from app.ams_data_processor import main
from infrastructure.output_writer import OutputWriter


def test_ams_processor_integration(tmpdir):
    """
        Integration test for the AMS processor main function.

        This test verifies the behavior of the AMS processor in an integration test environment.
        It simulates the execution of the main function and checks the output.
        """

    input_file = "infrastructure/test/data/c14-small.ams"
    output_dir = "../../output"
    with patch("infrastructure.output_writer.OutputWriter",
               return_value=OutputWriter(tmpdir)):
        main(input_file, "sum", output_dir)

        output_file = os.path.join(output_dir, "analyses_table_updated_data.html")
        assert os.path.exists(output_file)

        tmpdir.remove()


def test_main_invalid_file_format(capsys):
    """
        Test the behavior of the main function when an invalid file format is encountered.

        This test verifies that the main function raises a ValueError when an invalid file format
        is provided as a command-line argument. It checks the error message and ensures the program
        handles the error appropriately.
        """
    input_file = "infrastructure/test/data/c14-small.txt"
    output_dir = "../../output"

    main(input_file, "sum", output_dir)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "Error: Invalid file format." in output
