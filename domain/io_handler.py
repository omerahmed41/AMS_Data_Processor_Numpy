from infrastructure.file_reader_factory import FileReaderFactory
from infrastructure.output_writer import OutputWriter


def print_to_html(output_dir, analysis_array, modified_data, header):
    output_writer = OutputWriter(output_dir)
    output_writer.write_html_table(analysis_array, header, 'analyses_table_old_data.html')
    output_writer.write_html_table(modified_data, header, 'analyses_table_updated_data.html')


def read_file(file_path):
    file_reader = FileReaderFactory.create(file_path)
    return file_reader.read()
