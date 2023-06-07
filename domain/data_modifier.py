import pandas as pd
# pylint: disable=too-few-public-methods


class DataModifier:
    """
        Class for modifying data.

        This class provides a method to modify data according to a specified formula.

        Public Methods:
        - modify_data

        """
    def __init__(self, operation):
        self.operation = operation

    def modify(self, analysis_array):
        data_frame = pd.DataFrame(analysis_array)
        data_frame.iloc[::2] = data_frame.iloc[::2].applymap(self.operation.apply)
        return data_frame.to_numpy()
