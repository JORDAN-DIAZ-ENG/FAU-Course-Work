# This program strengthens skills in files and exceptions
def ed_append(filename, string):
    """ appends string to the end of the file, if file doesn't exist new file will be created with the filename. The
    function returns the number of characters written to the file """
    try:
        file = open(filename, "a")
        file.write(string)

        return len(string)
    except PermissionError:
        print("There was a permission Error")
    finally:
        file.close()


def ed_read(filename, fr=0, to=-1):
    """ returns as a string the content of the file named filename, with file positions in the half-open range [from,
    to). If to == -1 the content between from and the end of the file will be returned. If parameter to exceeds the
    file length, then the function raises exception IndexError with a corresponding error message """

    try:
        file = open(filename, "r")
        dumped_text = file.read()
        final_str = ""
        if to == -1:
            end_of_range = len(dumped_text)
        elif to > fr:
            end_of_range = to

        for i in range(fr, end_of_range):
            final_str += dumped_text[i]

        return final_str

    except FileNotFoundError:
        print("ERROR, File could not be found")
    except PermissionError:
        print("ERROR, Do not have permission to open file. May be used by another application")
    except IndexError:
        print("ERROR, parameter exceeds the file length")
    finally:
        file.close()


def ed_find(filename, search_str):
    """ finds search_str in the file named by filename and returns a list with index positions in the file text where
    the string search_str is located. E.g. it returns [4, 100] if the string was found at positions 4 and 100. it
    returns [] if the string was not found. """
    try:
        file = open(filename, "r")
        dumped_text = file.read()

        str_to_search = dumped_text

        final_list = [i for i in range(len(str_to_search)) if str_to_search.startswith(search_str, i)]

        return final_list

    except FileNotFoundError:
        print("ERROR, File could not be found")
    except PermissionError:
        print("ERROR, Do not have permission to open file. May be used by another application")
    except IOError:
        print("ERROR, There was an issue with I/O devices")
    finally:
        file.close()


def ed_replace(filename, search_str, replace_with, occurrence=-1):
    """ Replaces search_str in the file named by filename with string replace_with. If occurrence == -1,
    then it replaces ALL occurrences. If occurrence>=0, then it replaces only the occurrence with index occurrence,
    where 0 means the first, 1 means the second, etc. If the occurrence argument exceeds the actual occurrence index
    in the file of that string, the function does not do the replacement. The function returns the number of times
    the string was replaced. """
    try:
        file = open(filename, "r")
        dumped_text = file.read()

        lst_of_occurrences = ed_find(filename, search_str)
        if len(lst_of_occurrences) > 0:

            str_to_get = dumped_text[lst_of_occurrences[0]: lst_of_occurrences[0] + len(search_str)]

            times_replaced = 0

            if occurrence >= 0:
                final_text = dumped_text[:lst_of_occurrences[occurrence]] + replace_with + dumped_text[len(search_str) +
                                                                                                       lst_of_occurrences[
                                                                                                           occurrence]:]
                times_replaced = 1
            elif occurrence == -1:
                final_text = dumped_text.replace(str_to_get, replace_with)
                times_replaced = len(lst_of_occurrences)

            file2 = open(filename, "w")
            file2.write(final_text)

            return times_replaced
        else:
            print("Substring could not be found")

    except FileNotFoundError:
        print("ERROR, File could not be found")
    except PermissionError:
        print("ERROR, Do not have permission to open file. May be used by another application")
    except IOError:
        print("ERROR, There was an issue with I/O devices")
    finally:
        file.close()
        file2.close()


def testif(b, testname, msgOK="", msgFailed=""):
    """ Used for Unit Testing"""
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b


def test_ed_replace():
    """ Unit test for ed_replace"""
    fn = "test_ed_replace.txt"
    ed_append(fn, "bun lettuce cheese tomato patty bun")
    testif(ed_replace(fn, "lettuce", "", 0) == 1, "ed_replace with occurrence")
    testif(ed_replace(fn, "bun", "") == 2, "ed_replace without occurrence")
    # File Contents should be cheese tomato patty


def test_ed_find():
    """ Unit test for ed_replace"""
    fn = "test_ed_find.txt"
    ed_append(fn, "epicbyepicbyepicbyepicepic")
    testif(ed_find(fn, "epic") == [0, 6, 12, 18, 22], "ed_find when found")
    testif(ed_find(fn, "calculator") == [], "ed_find when not found")


def main():
    """ Main Function works as intended when files do not exist yet"""
    fn = "file.txt"

    ed_append(fn, "0123456789")  # this will create a new file
    ed_append(fn, "0123456789")  # the file content is: 01234567890123456789

    print(ed_read(fn, 3, 9))  # prints 345678. Notice that the interval excludes index to (9)
    print(ed_read(fn, 3))  # prints from 3 to the end of the file: 34567890123456789

    lst = ed_find(fn, "345")
    print(lst)  # prints [3, 13]
    print(ed_find(fn, "356"))  # prints []

    ed_replace(fn, "345", "ABCDE", 1)  # changes the file to 0123456789012ABCDE6789

    ed_replace(fn, "01", "popcorn")  # changes the file to popcorn23456789popcorn2ABCDE6789

    # Unit Testing
    test_ed_replace()
    test_ed_find()


if __name__ == "__main__":
    main()
