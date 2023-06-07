# pylint: disable=too-few-public-methods

import math


class IOperation:
    def apply(self, value):
        if value in ['nan', 'inf']:
            return value
        try:
            return self.perform_operation(float(value))
        except (ValueError, ZeroDivisionError):
            return value

    def perform_operation(self, value):
        raise NotImplementedError


class SumOperation(IOperation):
    def perform_operation(self, value):
        return f"++{value + (0.01 * value)}++"


class DivisionOperation(IOperation):
    def perform_operation(self, value):
        return f"//{1 / value}//"


class MultiplicationOperation(IOperation):
    def perform_operation(self, value):
        return f"**{value * value * 0.2}**"


class SquareRootOperation(IOperation):
    def perform_operation(self, value):
        return f"##{math.sqrt(value)}##"


class SubtractionOperation(IOperation):
    def perform_operation(self, value):
        return f"--{value - (0.01 * value)}--"


class NaturalLogarithmOperation(IOperation):
    def perform_operation(self, value):
        return f"..{math.log(value)}.."


class OperationFactory:
    def create(self, operation):
        if operation.lower() == "sum":
            return SumOperation()
        if operation.lower() == "division":
            return DivisionOperation()
        if operation.lower() == "multiplication":
            return MultiplicationOperation()
        if operation.lower() == "square root":
            return SquareRootOperation()
        if operation.lower() == "subtraction":
            return SubtractionOperation()
        if operation.lower() == "natural logarithm":
            return NaturalLogarithmOperation()
        raise ValueError("Invalid operation")
