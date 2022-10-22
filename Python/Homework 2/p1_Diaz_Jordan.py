# Jordan Diaz, This program manipulates files and parses itself
def line_number(file_name, write_to_this):
    """ This file takes the contents of one file and copies it into another file but with numbered lines """

    # edge case
    if file_name == write_to_this:
        print("Error: Cannot use the same file name")
        exit(1)

    try:
        # Open the files
        file_name = open(file_name, "r")
        write_to_this = open(write_to_this, "w")

        # Go through the file and write to the other
        count = 1
        for line in file_name:
            print(count, ". ", line, file=write_to_this, end="")
            count += 1

    except FileNotFoundError as er:
        print("The file: ", file_name, " does not exist.")
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    except PermissionError as er:
        print("You do not have access to read the file: ", file_name)
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    finally:
        # Close the files
        file_name.close()
        write_to_this.close()


def parse_functions(file_name):
    try:
        file_name = open(file_name, "r")

        separation_str = "def" + " "
        curr_function_str = ""

        count = 1
        lst_of_def_names = []
        lst_of_positions = []

        # Get the name of the function and the line number
        for line in file_name.readlines():

            for n in range(0, len(line)):
                avoid_str = "#" + " "
                if n == line.find(avoid_str) or n + 1 == line.find(avoid_str):
                    break
                elif n == line.find("    " + "#"):
                    break
                elif line.find(separation_str) != -1 and line[n - 1] == ":":
                    curr_function_str += "\n"
                elif line.find("def") == 0:
                    curr_function_str += line[n]
                elif line.find("    ") == 0:
                    curr_function_str += line[n]

            curr_name = ""

            # Build a list of positions and names of functions
            if line.find("def") == 0:
                for i in range(4, line.find("(")):
                    curr_name += line[i]
                lst_of_positions.append(count)
                lst_of_def_names.append(curr_name)

            count += 1

        separation_str = "def" + " "

        lst_of_functions = curr_function_str.split(separation_str)
        lst_of_functions.pop(0)

        for k in range(0, len(lst_of_functions)):
            lst_of_functions[k] = separation_str + lst_of_functions[k].replace("    ", "\t")

        final_lst = []
        for m in range(0, len(lst_of_def_names)):
            tple = (lst_of_def_names[m], lst_of_positions[m], lst_of_functions[m])
            final_lst.append(tple)

        final_lst.sort()
        return tuple(final_lst)

    except FileNotFoundError as er:
        print("The file: ", file_name, " does not exist.")
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    finally:
        file_name.close()


def main():
    line_number("p1_Diaz_Jordan.py", "test_file.txt")
    print(parse_functions("funs.py"))


if __name__ == "__main__":
    main()
