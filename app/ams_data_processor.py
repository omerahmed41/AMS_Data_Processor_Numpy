from domain.ams_processor import AMSProcessor
from domain.data_modifier import DataModifier
from domain.operations import OperationFactory
from infrastructure.file_reader_factory import FileReaderFactory
from infrastructure.output_writer import OutputWriter


def main(file_path, formula, output_dir):
    file_reader = FileReaderFactory.create(file_path)
    content = file_reader.read()

    ams_processor = AMSProcessor(content)
    analyses_data = ams_processor.extract_analyses_data()
    header, analysis_array = ams_processor.parse_analyses_data(analyses_data)

    operation = OperationFactory().create(formula)
    data_modifier = DataModifier(operation)
    modified_data = data_modifier.modify(analysis_array)

    output_writer = OutputWriter(output_dir)
    output_writer.write_html_table(analysis_array, header, 'analyses_table_old_data.html')
    output_writer.write_html_table(modified_data, header, 'analyses_table_updated_data.html')