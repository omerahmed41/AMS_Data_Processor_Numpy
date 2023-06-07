import os
from infrastructure.output_writer import OutputWriter


def test_output_writer():
    output_file = "./output/file_name.html"
    output_writer = OutputWriter("output")
    output_writer.write_html_table(["dummy_data"], ["dummy_header"], "file_name.html")
    assert os.path.exists(output_file)
    os.remove(output_file)


def test_output_writer_format():
    output_file = "./output/file_name.html"
    output_writer = OutputWriter("output")
    output_writer.write_html_table(["dummy_data"], ["dummy_header"], "file_name.html")
    with open(output_file, 'r', encoding='utf-8') as file:
        content = file.read()
        assert content.startswith("<table")
        assert content.endswith("</table>")
    os.remove(output_file)
