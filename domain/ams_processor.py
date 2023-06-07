import numpy as np
import re


class AMSProcessor:
    def __init__(self, content):
        self.content = content

    def extract_analyses_data(self):
        analyses_section = re.search(r'# Analyses(.*?)#', self.content, re.DOTALL)
        if analyses_section is None:
            raise ValueError("No analysis records found in the 'analyses' section.")
        analyses_data = analyses_section.group(1).strip().split('\n')

        if not analyses_data:
            raise ValueError("No analysis records found in the 'analyses' section.")
        return analyses_data

    def parse_analyses_data(self, analyses_data):
        analysis_array = np.array([row.split('\t') for row in analyses_data])

        header = analysis_array[0]
        analysis_array = analysis_array[1:]

        return header, analysis_array
