import pandas as pd


class DataModifier:
    def __init__(self, operation):
        self.operation = operation

    def modify(self, analysis_array):
        df = pd.DataFrame(analysis_array)
        df.iloc[::2] = df.iloc[::2].applymap(self.operation.apply)
        return df.to_numpy()