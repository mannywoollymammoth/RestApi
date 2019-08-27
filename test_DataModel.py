import unittest
from unittest.mock import patch
from DataModel import DataModel
import pandas as pd
from pandas.util.testing import assert_frame_equal
from collections import OrderedDict


class TestDataModel(unittest.TestCase):
    # this is a really long setup but i needed to have this so that i could properly compare the data
    def setUp(self):
        self.data = [['Martinez', 'Emmanuel', 'Male', 'Teal', '06/26/1996'],
                     ['Flores', 'Jenipher', 'Female', 'Black', '11/10/1994'],
                     ['Lomeli', 'Fernando', 'Male', 'Red', '06/26/1993'],
                     ['Fonseca', 'Adrian', 'Male', 'Black', '11/10/1980']]

        birthdate_data = OrderedDict([("LastName", ["Fonseca", "Lomeli", "Flores", "Martinez"]),
                                      ("FirstName", [
                                       "Adrian", "Fernando", "Jenipher", "Emmanuel"]),
                                      ("Gender", [
                                       "Male", "Male", "Female", "Male"]),
                                      ("FavoriteColor", [
                                       "Black", "Red", "Black", "Teal"]),
                                      ("DateOfBirth", [
                                       "11/10/80", "06/26/93", "11/10/94", "06/26/96"])
                                      ])

        self.birthdate_data_frame = pd.DataFrame(
            birthdate_data, columns=birthdate_data.keys())

        gender_data = OrderedDict([("LastName", ["Flores", "Fonseca", "Lomeli",  "Martinez"]),
                                   ("FirstName", [
                                       "Jenipher", "Adrian", "Fernando",  "Emmanuel"]),
                                   ("Gender", [
                                       "Female", "Male", "Male",  "Male"]),
                                   ("FavoriteColor", [
                                       "Black", "Black", "Red",  "Teal"]),
                                   ("DateOfBirth", [
                                       "11/10/1994", "11/10/1980", "06/26/1993",  "06/26/1996"])
                                   ])

        self.gender_data_frame = pd.DataFrame(
            gender_data, columns=gender_data.keys())

        name_data = OrderedDict([("LastName", ["Flores", "Fonseca", "Lomeli",  "Martinez"]),
                                 ("FirstName", [
                                     "Jenipher", "Adrian", "Fernando",  "Emmanuel"]),
                                 ("Gender", [
                                     "Female", "Male", "Male",  "Male"]),
                                 ("FavoriteColor", [
                                     "Black", "Black", "Red",  "Teal"]),
                                 ("DateOfBirth", [
                                     "11/10/1994", "11/10/1980", "06/26/1993",  "06/26/1996"])
                                 ])

        self.name_data_frame = pd.DataFrame(
            name_data, columns=name_data.keys())

        self.data_frame = pd.DataFrame(self.data, columns=[
                                       'LastName', 'FirstName', 'Gender', 'FavoriteColor', 'DateOfBirth'])
        self.input_path_list = ['testdata1.csv', 'testdata2.csv']
        self.data_model_object = DataModel(self.input_path_list)

    # TESTS
    def test_read_files_and_merge(self):
        data_model_object_local = DataModel(self.input_path_list)
        assert_frame_equal(data_model_object_local.records, self.data_frame)

    def test_sort_by_birthdate(self):
        birthdate_sort = self.data_model_object.sort_by_birthdate()
        assert_frame_equal(birthdate_sort, self.birthdate_data_frame)

    def test_sort_by_gender(self):
        gender_sort = self.data_model_object.sort_by_gender()
        assert_frame_equal(gender_sort, self.gender_data_frame)

    def test_sort_by_name(self):
        name_sort = self.data_model_object.sort_by_name()
        assert_frame_equal(name_sort, self.name_data_frame)


if __name__ == '__main__':
    unittest.main()
