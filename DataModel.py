import pandas as pd


class DataModel:

    # Initializer / Instance Attributes
    def __init__(self, input_path_list):
        self.records = self.read_files_and_merge(input_path_list)

    # TODO: add error checking to make sure that the files are only in the
    # 3 acceptable formats
    def read_files_and_merge(self, input_path_list):
        data_frame = pd.concat(
            [pd.read_csv(input_path, sep='[,| ]+', engine='python')
             for input_path in input_path_list], ignore_index=True
        )
        return data_frame

    # TODO: figure out how to sort this shit
    def sort_by_gender(self):
        gender_records = self.records.sort_values(by=['Gender', 'LastName'])
        return gender_records

    def sort_by_birthdate(self):
        bday_records = self.records
        bday_records['DateOfBirth'] = pd.to_datetime(
            bday_records['DateOfBirth'])
        bday_records = bday_records.sort_values(by=['DateOfBirth'])
        bday_records['DateOfBirth'] = bday_records['DateOfBirth'].dt.strftime(
            '%m/%d/%y')
        return bday_records

    def sort_by_name(self):
        name_records = self.records.sort_values(by=['LastName'])
        return name_records
