# Jordan Diaz, This program involves csv files
import csv


def add_contact(contacts, info_tuple):
    """ adds a contact to an already existing list of contacts"""
    for contact in contacts:
        if info_tuple[0] == contact[0]:
            contacts.remove(contact)
            contacts.append(info_tuple)
            contacts.sort()
            return False
    contacts.append(info_tuple)
    contacts.sort()
    return True


def remove_contact(contacts, info_tuple):
    """ Removes a specific contact from a list of contacts"""
    if info_tuple in contacts:
        contacts.remove(info_tuple)
        return True
    return False


def find_contact(contacts, name=None, nickname=None):
    """ Finds a specific contact in a list of contact the name or nickname, must specify"""
    for contact in contacts:
        if name is not None:
            if contact[0] == name:
                return contact
        elif nickname is not None:
            if contact[1] == nickname:
                return contact


def save_to_csv(contacts, file_name):
    """ This function changes the contents of a file to match a list of contacts"""
    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)

            for contact in contacts:
                writer.writerow([contact[0], contact[1], contact[2]])

    except FileNotFoundError as er:
        print("The file: ", file_name, " does not exist.")
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    except PermissionError as er:
        print("You do not have access to open the file: ", file_name)
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    finally:
        file.close()


def read_from_csv(file_name):
    """ This function reads from a csv file and returns a list of tuples that has the contents of the file"""
    try:
        with open(file_name, "r") as file:

            # Read file and create a list of contacts, then returns that list
            reader = csv.reader(file)
            contacts_in_file = []
            for line in reader:
                contacts_in_file.append((line[0], line[1], line[2]))
            return contacts_in_file

    except FileNotFoundError as er:
        print("The file: ", file_name, " does not exist.")
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    except PermissionError as er:
        print("You do not have access to read the file: ", file_name)
        print("Exception type: {} : the error message was {} ".format(type(er), er))

    finally:
        file.close()


def testif(b, test_name, msg_ok="", msg_failed=""):
    """ This runs tests to reach the desired outcome of a function"""
    if b:
        print("Success:   " + test_name + "; " + msg_ok)
    else:
        print("Failed:   " + test_name + "; " + msg_failed)
    return b


def main():
    """ This is the main function, testing all the applicatons of the functions"""
    # Test if you a contact is replaced and returns False
    contact_lst = []
    add_contact(contact_lst, ("Earl Simmons", "DMX", "305-1010101"))
    testif(add_contact(contact_lst, ("Earl Simmons", "DMX", "999-987654321")) == False and contact_lst == [
        ("Earl Simmons", "DMX", "999-987654321")], "Test 1")

    # Test if a contact does not exist it will add it in alphabetical order and return true
    testif(add_contact(contact_lst, ("Robert", "Rob", "123,3211233219")) == True and contact_lst == [
        ("Earl Simmons", "DMX", "999-987654321"), ("Robert", "Rob", "123,3211233219")], "Test 2")

    # Test if a contact is removed it will return true
    testif(remove_contact(contact_lst, ("Robert", "Rob", "123,3211233219")) == True and contact_lst == [
        ("Earl Simmons", "DMX", "999-987654321")], "Test 3")

    # tests if a contact does not exist it will return False
    testif(remove_contact(contact_lst, ("Robert", "Rob", "123,3211233219")) == False and contact_lst == [
        ("Earl Simmons", "DMX", "999-987654321")], "Test 4")

    # tests if find contact returns the tuple using a name
    testif(find_contact(contact_lst, name="Earl Simmons") == ("Earl Simmons", "DMX", "999-987654321"), "Test 5")

    # tests if find contact returns the tuple using a nickname
    testif(find_contact(contact_lst, nickname="DMX") == ("Earl Simmons", "DMX", "999-987654321"), "Test 6")

    # Tests if cannot find contact it will return None
    testif(find_contact(contact_lst, name="fred", nickname="freddy") is None, "Test 7")

    # Tests if read and write to csv works
    contact_lst = []

    add_contact(contact_lst, ("Earl Simmons", "DMX", "305-1010101"))
    add_contact(contact_lst, ("Beyonce Knowles", "bey", "561-1234321"))
    add_contact(contact_lst, ("Cardi B", "Belcalis", "305-4399521"))

    save_to_csv(contact_lst, "test.csv")

    testif(
        read_from_csv("test.csv") == [('Beyonce Knowles', 'bey', '561-1234321'), ('Cardi B', 'Belcalis', '305-4399521'),
                                      ('Earl Simmons', 'DMX', '305-1010101')], "Test 8")


if __name__ == "__main__":
    main()
