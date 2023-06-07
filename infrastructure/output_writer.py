import os
import pandas as pd


class OutputWriter:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def write_html_table(self, analysis_array, header, output_filename):
        data_frame = pd.DataFrame(analysis_array, columns=header)
        html = data_frame.to_html()

        output_file_path = os.path.join(self.output_dir, output_filename)
        with open(output_file_path, "w",  encoding='utf-8') as file:
            file.write(html)
        print(f"Results have been written to {output_file_path}.")
