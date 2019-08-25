import DataModel as dm


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
            if input_path != 'q':
                input_path_list.append(input_path)

        return input_path_list

        # data_model = dm.DataModel(input_path_list)
        # print(data_model.records)


# if __name__ == "__main__":
#     cmd_line_interface = CommandLineInterface()
#     cmd_line_interface.prompt()
