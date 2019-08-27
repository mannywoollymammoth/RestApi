import pandas as pd
import copy
import re

# DataModel is in charge of formatting the data for the requests
# Because I want the data to change as little as possible I am making deep copies
# of the dataframe and outputting a different object that will be garbage collected
# later anyways


class DataModel:

    # Initializer / Instance Attributes
    def __init__(self, input_path_list):
        self.records = self.read_files_and_merge(input_path_list)

    # TODO: add error checking to make sure that the files are only in the
    def read_files_and_merge(self, input_path_list):
        data_frame = pd.concat(
            [pd.read_csv(input_path, sep='[,| ]+', engine='python')
             for input_path in input_path_list], ignore_index=True
        )
        return data_frame

    def sort_by_gender(self):
        gender_records = copy.deepcopy(self.records)
        gender_records = gender_records.sort_values(by=['Gender', 'LastName'])
        return gender_records

    def sort_by_birthdate(self):
        bday_records = copy.deepcopy(self.records)
        bday_records['DateOfBirth'] = pd.to_datetime(
            bday_records['DateOfBirth'])
        bday_records = bday_records.sort_values(by=['DateOfBirth'])
        bday_records['DateOfBirth'] = bday_records['Date
                                                   OfBirth'].dt.strftime(
            '%m/%d/%y')
        return bday_records

    def sort_by_name(self):
        name_records = copy.deepcopy(self.records)
        name_records = name_records.sort_values(by=['LastName'])
        return name_records

    # this function will get the line from the user and then
    # verifying that it has enough fields and then appending it to
    # the data data frame
    # TODO: make sure that we check that the date field is in correct format
    def add_line_to_record(self, line):
        line = line.decode("utf-8")
        line = re.compile('[,| ]+').split(line)
        if len(line) == 5:
            last_name = line[0]
            first_name = line[1]
            gender = line[2]
            favorite_color = line[3]
            date_of_birth = line[4]
            record = {'LastName': last_name, 'FirstName': first_name, 'Gender': gender,
                      'FavoriteColor': favorite_color, 'DateOfBirth': date_of_birth}
            self.records = self.records.append(record, ignore_index=True)

            print(self.records)
            return True
        else:
            return False
