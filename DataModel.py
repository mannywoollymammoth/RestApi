import pandas as pd
class DataModel:

    # Initializer / Instance Attributes
    def __init__(self, input_path_list):
        self.data_frame = pd.read_csv(input_path)
