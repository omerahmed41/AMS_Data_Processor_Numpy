import os
from unittest.mock import patch
from app.ams_data_processor import main
from infrastructure.output_writer import OutputWriter


def test_ams_processor_integration(tmpdir):
    input_file = "infrastructure/test/data/c14-small.ams"
    output_dir = "../../output"
    with patch("infrastructure.output_writer.OutputWriter",
               return_value=OutputWriter(tmpdir)):
        main(input_file, "sum", output_dir)

        # Check if the output file is created
        output_file = os.path.join(output_dir, "analyses_table_updated_data.html")
        assert os.path.exists(output_file)

        # Clean up the temporary directory
        tmpdir.remove()


def test_main_invalid_file_format(capsys):
    input_file = "infrastructure/test/data/c14-small.txt"
    output_dir = "../../output"

    main(input_file, "sum", output_dir)

    # Capture the printed output
    captured = capsys.readouterr()
    output = captured.out.strip()

    # Verify the error message
    assert "Error: Invalid file format." in output