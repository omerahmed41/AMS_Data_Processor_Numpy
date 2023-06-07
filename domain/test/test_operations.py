import pytest
from domain.operations import OperationFactory


def test_operation_factory():
    operation = OperationFactory().create("sum").apply
    assert operation(5) == "++5.05++"
    with pytest.raises(ValueError):
        OperationFactory().create("unsupported_operation")


def test_operation_factory_edge_cases():
    operation = OperationFactory().create("Division").apply
    assert operation(0) == 0  # Division by zero
    assert operation(-1) == "//-1.0//"  # Division by a negative number
    assert operation('inf') == 'inf'  # Division by infinity

    operation = OperationFactory().create("Natural logarithm").apply
    assert operation(0) == 0  # Logarithm of zero
    assert operation(1) == '..0.0..'  # Logarithm of one
    assert operation(float('inf')) == '..inf..'  # Logarithm of infinity


def test_invalid_formula():
    with pytest.raises(ValueError):
        operation = OperationFactory().create("invalid_formula")