import pytest


@pytest.fixture(name="mock_file_content")
def fixture_mock_file_content():
    return "# Analyses\n1\t2\t3\n4\t5\t6\n#"
