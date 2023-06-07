import os
from unittest.mock import patch
from app.ams_data_processor import main
from infrastructure.output_writer import OutputWriter

# Test file paths
input_file = "infrastructure/test/data/c14-small.ams"
output_dir = "../../output"


def test_ams_processor_integration(tmpdir):
    with patch("infrastructure.output_writer.OutputWriter",
               return_value=OutputWriter(tmpdir)):
        main(input_file, "sum", output_dir)

        # Check if the output file is created
        output_file = os.path.join(output_dir, "analyses_table_updated_data.html")
        assert os.path.exists(output_file)

        # Clean up the temporary directory
        tmpdir.remove()
