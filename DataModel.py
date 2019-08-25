import pandas as pd


class DataModel:

    # Initializer / Instance Attributes
    def __init__(self, input_path_list):
        self.records = self.read_files_and_merge(input_path_list)

    # TODO: add error checking to make sure that the files are only in the
    # 3 acceptable formats
    def read_files_and_merge(self, input_path_list):
        data_frame = pd.concat(
            [pd.read_csv(input_path, sep=None, engine='python')
             for input_path in input_path_list]
        )
        return data_frame
