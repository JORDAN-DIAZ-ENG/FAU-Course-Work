#
# COP4045 Python
# Homework 3
# Do not distribute.
# Author: Ionut Cardei
#

import sys

# tuple positions:
IDX_NAME = 0
IDX_NICKNAME = 1
IDX_TEL = 2

# a)

def contacts_add(cont_lst:list, name:str, nickname:str="", tel:str=""):
    """ Adds or modifies a contact entry.
        Returns True of new contact inserted or False if existing contact was modified.
        Parameter cont_lst:  the contact list
        Parameter name: the contact's name
        Parameter nickname: the nickname
        Precondition: name and nickname are not both blank or ""
        Postcondition: tuple with given name modified or inserted.
    """
    if name == "" and nickname == "":
        print(__name__ + " ERROR: both name and nickname are ''.", file=sys.stderr)
        exit(1)
    inserted = False
    i = 0
    if name != "":
        while (i < len(cont_lst)) and name > cont_lst[i][IDX_NAME]:
            i = i + 1
    else:   # use nickname
        while (i < len(cont_lst)) and nickname != cont_lst[i][IDX_NICKNAME]:
            i = i + 1
        
    if i < len(cont_lst) and (name == cont_lst[i][IDX_NAME] or nickname == cont_lst[i][IDX_NICKNAME]):
        # replace entry:
        cont_lst[i] = (name, nickname, tel)
    else:
        cont_lst.insert(i, (name, nickname, tel))
        inserted = True
    cont_lst.sort()    # sort on name entry
    return inserted
                   

# b)
def contacts_remove(cont_lst:list, name:str=""):
    """Remove a contact from a contact list given its name.
       Parameter cont_lst: the contact list
       Parameter name: the contact's name
       Precondition: 
       Postcondition: contact list modifier if contact existed before.
    """
    # trivial implementation with linear search in O(N):
    cont_tup = contacts_find(cont_lst, name)
    removed = False
    if cont_tup:
        cont_lst.remove(cont_tup)
        removed = True
    return removed
        


# c)

def contacts_find(cont_lst:list, name:str="", nickname:str=""):
    """Finds a contact in a contact list given name or nickname.
       Parameter cont_lst: the contact list
       Parameter name: the contact's name
       Parameter nickname: the nickname
       Precondition: name and nickname are not both blank or ""
       Postcondition: none; the list is not modified.
    """
    # strip whitespace:
    name = name.strip()
    nickname = nickname.strip()
    if name == "" and nickname == "":
        print(__name__ + " ERROR: both name and nickname are ''.", file=sys.stderr)
        exit(1)

    # this is a trivial O(N) algorithm. Using binary search (with name) could reduce complexity to O(log N)
    for (cname, cnickname, tel) in cont_lst:
        if (name != "" and cname == name) or (nickname != "" and cnickname == nickname):
            return (cname, cnickname, tel)
    return None   # none found



# d)

def contacts_save(cont_lst:list, filename:str):
    """ Save contact list to a file.
        Parameter cont_lst: the contact list
        Parameter filename: the filename
        Precondition: cont_lst has the correct format and the user has write permission for the given file name.
        Postcondition: contact list saved written to file.
    """
    try:
        separator = "|"             # field separator; comma is too common in names, so we use something else
        fout = open(filename, "w")
        for contact in cont_lst:    # contact is a tuple
            line = separator.join(contact)
            fout.write(line)
            fout.write("\n")
        fout.close()
    except FileNotFoundError as exc:
        print("Error: input file {} not found.\n".format(filename), file=sys.stderr)
        raise exc 
    except IOError as exc:
        print("Error: IOError while working with file {}.\n".format(filename), file=sys.stderr)
        raise exc 

        
#e)
def contacts_load(filename:str):
    """ Read contact list from a file.
        Returns: the contact list
        Parameter filename: the source filename
        Precondition: the file has the correct format and the user has read permission for the given file name.
        Postcondition: contact list saved written to file.
    """
    try:
        separator = "|"             # field separator; comma is too common in names, so we use something else
        fin = open(filename, "r")
        cont_lst = list()
        for line in fin:
            contact = line.rstrip().split(separator)   # rstrip gets rid of \n
            cont_lst.append(tuple(contact))         # contact is a list; we need a tuple.
        fin.close()
    except FileNotFoundError as exc:
        print("Error: input file {} not found.\n".format(filename), file=sys.stderr)
        raise exc 
    except IOError as exc:
        print("Error: IOError while working with file {}.\n".format(filename), file=sys.stderr)
        raise exc 
    cont_lst.sort()     # sorts by the first element each tuple, the name
    return cont_lst
    
cl = [("Beyonce Knowles", "bey", "561-1234321"), ("Cardi B", "Belcalis", "305-4399521"), ("Earl Simmons", "DMX", "305-1010101")]



def main():
    filename = "contacts.csv"
    contacts_save(cl, filename)
    
    with open(filename, "r") as f:
        filecontents = f.read()

    if filecontents != 'Beyonce Knowles|bey|561-1234321\nCardi B|Belcalis|305-4399521\nEarl Simmons|DMX|305-1010101\n':
        print("ERROR: save failed.")
        exit(1)

    # test load:    
    cl2 = contacts_load("contacts.csv")    
    if cl2 != cl:
        print("ERROR: save/restore failed.")
        exit(2)

    cont1 = contacts_find(cl, name="Cardi B")
    cont2 = contacts_find(cl, nickname="Belcalis")
    cont22 = contacts_find(cl, nickname="wrong nickname")
    if cont1 != ("Cardi B", "Belcalis", "305-4399521") or cont1 != cont2 or cont22 != None:
        print("ERROR: find failed.")
        exit(3)

    # test add:
    #cont3 = ("Christopher Bridges", "Ludacris", "305-555-4LUDA")
    contacts_add(cl2, "Christopher Bridges", "Ludacris", "305-555-4LUDA")
    cont4 = contacts_find(cl2, nickname="Ludacris")
    if cont4 == None:
        print("ERROR (2): find failed.")
        exit(4)

    # test remove:
    removed = contacts_remove(cl2, "Christopher Bridges")
    cont5 = contacts_find(cl2, name="Christopher Bridges")
    if not removed or cont5 != None:
        print("ERROR: remove failed.")
        exit(5)
       
    print("All tests passed.")
    
