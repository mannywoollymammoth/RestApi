# this class is responsible for all the user interaction
# will return a list of files for the data model to parse through


class CommandLineInterface:
    # TODO: Verify whether the files that are being entered are valid
    # Program will start here prompting user for input until they enter q to quit
    def prompt(self):
        input_path = ""
        input_path_list = []

        print("Program is starting")
        while input_path != 'q':
            print("When you are done please enter ")
            print("Enter the file path with name. Example  \"/home/manny/Documents\"")
            input_path = input()
            if input_path != 'q':
                input_path_list.append(input_path)

        return input_path_list

    def check_if_files_are_valid():
        pass
