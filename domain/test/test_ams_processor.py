from domain.ams_processor import AMSProcessor


def test_ams_processor(mock_file_content):
    ams_processor = AMSProcessor(mock_file_content)
    analyses_data = ams_processor.extract_analyses_data()
    assert analyses_data == ['1\t2\t3', '4\t5\t6']
    header, analysis_array = ams_processor.parse_analyses_data(analyses_data)
    assert (header == ['1', '2', '3']).all()
    assert (analysis_array == [['4', '5', '6']]).all()