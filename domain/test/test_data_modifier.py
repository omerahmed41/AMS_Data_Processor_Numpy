from domain.data_modifier import DataModifier
from domain.operations import OperationFactory


def test_data_modifier():
    operation = OperationFactory().create("sum")
    data_modifier = DataModifier(operation)
    analysis_array = [['1', '2', '3'], ['4', '5', '6']]
    modified_array = data_modifier.modify(analysis_array)
    assert (modified_array == [['++1.01++', '++2.02++', '++3.03++'], ['4', '5', '6']]).all()