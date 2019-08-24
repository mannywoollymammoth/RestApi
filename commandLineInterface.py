import DataModel as dm
class CommandLineInterface:
    # Program will start here prompting user for input until they enter q to quit
    def prompt(self):
        input_path = ""
        input_path_list = []
        #print("Enter the file path with name. Example  \"/home/manny/Documents\"")
        #input_path = input()
        #data_model = dm.DataModel(input_path)
        #print(data_model.data_frame)

        print("Program is starting")
        while input_path != 'q':
            print("When you are done please enter 'q'")
            print("Enter the file path with name. Example  \"/home/manny/Documents\"")
            input_path = input()
            input_path_list.append(input_path)

        data_model = dm.DataModel(input_path_list)

    # TODO: create a function that will run once an initialize things
    # then a second function that will be constantly looping through
    # this prevents there from being multiple initializations

if __name__ == "__main__":
    cmd_line_interface = CommandLineInterface()
    cmd_line_interface.prompt()
