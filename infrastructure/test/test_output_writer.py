import os
from infrastructure.output_writer import OutputWriter


def test_output_writer():
    output_file = "./output/file_name.html"
    output_writer = OutputWriter("output")
    output_writer.write_html_table(["dummy_data"], ["dummy_header"], "file_name.html")
    assert os.path.exists(output_file)