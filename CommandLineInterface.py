# this class is responsible for all the user interaction
# will return a list of files for the data model to parse through
import os.path
from os import path


class CommandLineInterface:
    # Program will start here prompting user for input until they enter q to quit
    def prompt(self):
        input_path = ""
        input_path_list = []

        print("Program is starting")
        while input_path != 'q':
            print("When you are done please enter ")
            print("Enter the file path with name. Example  \"/home/manny/Documents\"")
            input_path = input()
            self.check_if_files_are_valid(input_path, input_path_list)

        return input_path_list

    def check_if_files_are_valid(self, input_path, input_path_list):
        if path.exists(input_path):
            input_path_list.append(input_path)
        else:
            print('That file is not found')
