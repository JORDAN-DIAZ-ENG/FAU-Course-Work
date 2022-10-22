# COP 4045 Python Programming
# Author Ionut Cardei
# Do not distribute

# Homework 4

import os
from testif import testif

# info for two test files:
test0name = "test0.txt"
test0data = "0123456789"
test1name = "test1.txt"
test1data = "0123423567238"

def make_testfile(fn, s):
    """Creates a test file with repeated substrings."""
    with open(fn, "w") as f:
        f.write(s)

def make_test1file():
    make_testfile(test1name, test1data)

def remove_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

make_testfile(test0name, test0data)

    


def ed_read(filename, start=0, to=-1):
    """Returns as a string the content of the file named filename,
    with file positions in the half-open range [start, to).
    If to==-1, the function returns the entire file.
    precondition: start >= 0 and (to >= 0 or to == -1)
    """
    s = ""
    if start < 0:
        raise ValueError("invalid value for start param")
    if to < 0 and to != -1:
        raise ValueError("invalid value for to param")
    
    if to == -1 or start < to:    
        with open(filename, "r") as f:
            filecontent = f.read()
            if to > len(filecontent):
                raise ValueError("invalid value for to param")
            s = filecontent[start:to] if to > 0 else filecontent[start:]
    return s

def test_read():
    testif(ed_read(test0name) == test0data, "ed_read: all file")
    testif(ed_read(test0name, 3,9) == test0data[3:9], "ed_read: slice")
    testif(ed_read(test0name, 5,3) == "", "ed_read: start > to")
    testif(ed_read(test0name, 3,9) == test0data[3:9], "ed_read: slice")

    try:
        ed_read(test0name, -3, -1)
        testif(False, "ed_read: exception for start<0")
    except ValueError:
        testif(True, "ed_read:exception for start<0")


def ed_find(filename, search_str):
    """finds string search_str in the file named by filename and returns a
    list with index positions in the file text where the string search_str is located
    """
    filecontent = ed_read(filename)
    found_lst = []   # stores indices where found or []
    idx = 0    # search from this position
    while True:
        idx = filecontent.find(search_str, idx)
        if idx < 0:
            break
        found_lst.append(idx)  # got one position
        idx += 1               # keep searching from the next character in the content
    return found_lst

def test_find():
    make_test1file()
    testif(ed_find(test1name, "23") == [2, 5, 10], "ed_find: found")
    testif(ed_find(test1name, "XY") == [], "ed_find: not found")
    

def ed_replace(filename, search_str, replace_with, occurrence=-1):
    """ replaces search_str in the file
    named by filename with string replace_with.
    If occurrence==-1, then it replaces ALL occurrences.
    If occurrence>=0, then it replaces only the occurrence with index occurrence, where 0 means the
    first, 1 means the second, etc.
    If the occurrence argument exceeds the actual occurrence index in
    the file of that string, the function does not do the replacement.
    The function returns the number of times the string was replaced.
    """
    if search_str == "":
        return 0

    filecontent = ed_read(filename)

    # it is more efficient to construct a new string using a list of substrings 
    # that is joined at the end in one string (O(N)) than
    # keeping a string that is "grown" with += or similar (O(M*N))
    newcontent_lst = []     # list stores chunks of the new content
    count = 0
    occ = 0    # current replacement index
    idx = 0    # search from this position
    prev_start = 0    # previous start of original string
    prev_search = 0
    while True:
        idx = filecontent.find(search_str, prev_search)
        if (idx == -1):
            # no more replacements (if any):            
            break
        if (occurrence == -1) or (occ == occurrence):
            newcontent_lst.append(filecontent[prev_start:idx])
            newcontent_lst.append(replace_with)
            prev_start = idx + len(search_str)
            count += 1
            if occ == occurrence:    # one replacement and done!
                break
        prev_search = idx + 1     # keep searching from the next character
        occ += 1

    newcontent_lst.append(filecontent[prev_start:])   # add remainder to end
    newcontent = "".join(newcontent_lst)
    #print(newcontent)
    ed_write(filename, newcontent)
    return count
                                  
        
def test_replace():
    make_test1file()
    toreplace = "23"
    r = "XYZ"
    count = ed_replace(test1name, toreplace, r, -1)
    testif(count == 3 and ed_read(test1name) == test1data.replace(toreplace, r),
           "ed_replace: all")

    # reset test:
    make_test1file()    
    count = ed_replace(test1name, toreplace, r, 0)
    testif(count == 1 and ed_read(test1name) == test1data.replace(toreplace, r, 1),
           "ed_replace: first")

    make_test1file()
    count = ed_replace(test1name, toreplace, r, 2)
    testif(count == 1 and ed_read(test1name) == "0123423567"+r+"8",
           "ed_replace: third")
    

def ed_append(filename, s):
    """Appends string to the end of the file. If the file does not exist, a new
    file is created with the given file name. The function returns the number of characters written to the
    file.
    """
    with open(filename, "a") as f:
        return f.write(s)

# unit test for append.
# This is superficial - it does not deal with file I/O errors.
def test_append():
    test_name = "ed_append"
    test_fn = "test.txt"     # test file name
    remove_file(test_fn)            # start from scratch each test, with a brand new file.
        
    # write some initial content to the file
    initial_text = "ABCD"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)

    # now test ed_append:
    try:
        new_text = "01234"
        # our test subject:    
        ret = ed_append(test_fn, new_text)
    
        expected_text = initial_text + new_text

        # we need to check returned value and that the file has changed accordingly:
        current_text = open(test_fn, "r").read()   # read entire file

        # test the condition:
        cond = (ret == len(new_text)) and (current_text == expected_text)
        
        testif(cond, test_name)
    except Exception as exc:           # catch all
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        


def ed_write(filename, tup_or_str):
    """For each tuple (position, s) in collection pos_str_col (e.g. a list)
    this function writes to the file at position pos the string s. This function overwrites some of the
    existing file content. If any position parameter is invalid (< 0) or greater than the file contents size,
    the function does not change the file and raises ValueError with a proper error message. In case of
    no errors, the function returns the number of strings written to the file.
    If the file doesn't exist it throws exception
    
    Precondition:  strings do not overlap.

    If the parameter is a string, then the entire file is overwritten with the string.

    Note: this type of write operation is called  "scattered".
    """
    if type(tup_or_str) == str:
        with open(filename, "w") as f:   # overwrite
            f.write(tup_or_str)
            return 1
    elif type(tup_or_str) in (list, tuple):
        with open(filename, "r") as f:     
            f.seek(0)
            filecontent = f.read()
        with open(filename, "w") as f:                 
            f.seek(0)
            # check params:
            for (pos, s) in tup_or_str:
                # pos can be == len(filecontent): this will append at the end
                if not 0 <= pos <= len(filecontent):
                    raise ValueError("Invalid position argument {}".format(pos))

            # sort tuples based on position:
            tup_or_str = sorted(tup_or_str)

            # check for overlapping writes:
            idx = 0
            for (pos,s) in tup_or_str:
                if pos < idx:
                    raise ValueError("Overlapping write for ({},{})".format(pos, s))
                idx = pos + len(s)
                
            # assemble the new file content from chunks in a list:
            newcontent_lst = []
            prev_start = 0
            count = 0
            for (pos, s) in tup_or_str:
                newcontent_lst.append(filecontent[prev_start:pos])
                newcontent_lst.append(s)
                prev_start = pos + len(s)
                count += 1

            newcontent_lst.append(filecontent[prev_start:]) # add remainder
            newcontent = "".join(newcontent_lst)
            f.write(newcontent)
            return count    # "with" context mngr will close f.
            
    else:
        raise ValueError("Invalid argument type")
        

def test_write():
    # test writing new file:
    remove_file(test1name)
    s = "0123456789"
    r = ed_write(test1name, s)
    testif(r==1 and ed_read(test1name)==s, "ed_write: new file")

    out_tups = [(0, "ABC"), (6, "D"), (10, "EFG")]
    r = ed_write(test1name, out_tups)
    testif(r==len(out_tups) and ed_read(test1name)=="ABC345D789EFG", "ed_write: tuples")

    # now check error handling:
    r = ed_write(test1name, s)
    try:
        r = ed_write(test1name, ((2, "x"), (len(s) + 1, "x"), (4, "xx")))
        # test failed:
        testif(False, "ed_write: handle invalid position")
    except ValueError:
        testif(True, "ed_write: handle invalid position")

    # check finding overlapping writes:
    try:
        r = ed_write(test1name, ((2, "x"), (9, "XYZ"), (5, "xx"),  (3, "ABCD")))
        # test failed:
        testif(False, "ed_write: handle overlapping writes")
    except ValueError:
        testif(True, "ed_write: handle overlapping writes")
    
def ed_insert(filename, pos_str_col):
    """For each tuple (position, s) in collection pos_str_col (e.g. a list)
    this function inserts into to the file content the string s at position pos.
    This function does not overwrite the existing file content.
    If any position parameters is invalid (< 0) or greater than the original file content length,
    the function does not change the file at all and raises ValueError with a proper error
    message.
    
    In case of no errors, the function returns the number of strings inserted to the file.
    """
    # sort tuples based on position:
    pos_str_col = sorted(pos_str_col)

    # is this a new file?
    if os.path.isfile(filename):
        with open(filename, "r+") as f:
            filecontent = f.read()
            f.seek(0)
            # check params:
            for (pos, s) in pos_str_col:
                # pos can be == len(filecontent): this will append at the end
                if not 0 <= pos <= len(filecontent):
                    raise ValueError("Invalid position argument {}".format(pos))
                
            # assemble the new file content from chunks in a list:
            newcontent_lst = []
            prev_start = 0
            count = 0
            for (pos, s) in pos_str_col:
                newcontent_lst.append(filecontent[prev_start:pos])
                newcontent_lst.append(s)
                prev_start = pos
                count += 1

            newcontent_lst.append(filecontent[prev_start:]) # add remainder
            newcontent = "".join(newcontent_lst)
            f.write(newcontent)
            return count    
    elif pos_str_col[0][0] == 0:   # new file: write only what is at position 0
        with open(filename, "w") as f:
            f.write(pos_str_col[0][1])
        return 1
    else:
        return 0

    

def test_insert():
    remove_file(test1name)
    r = ed_insert(test1name, [(0, test0data)])
    testif(r==1 and ed_read(test1name)==test0data, "ed_insert: new file")

    remove_file(test1name)
    ed_write(test1name, test0data)
    out_tups = [(0, "ABC"), (6, "D"), (10, "EFG")]
    r = ed_insert(test1name, out_tups)
    testif(r==len(out_tups) and ed_read(test1name)=="ABC012345D6789EFG", "ed_insert: tuples")
    
    # now check error handling:
    r = ed_write(test1name, test0data)
    try:
        r = ed_insert(test1name, ((2, "x"), (len(test0data) + 1, "x"), (4, "xx")))
        # test failed:
        testif(False, "ed_insert: handle invalid position")
    except ValueError:
        testif(True, "ed_insert: handle invalid position")

  

def run_tests():
    test_read()
    test_write()
    test_find()
    test_replace()
    test_append()
    test_insert()
    

run_tests()
remove_file(test0name)
remove_file(test1name)

# used for the homework description:
def main_demo():
    fn = "file1.txt"    # assume this file does not exist yet.
    ed_append(fn, "0123456789")    # this will create a new file
    ed_append(fn, "0123456789")    # the file content is: 01234567890123456789

    print(ed_read(fn, 3, 9))    # prints 345678
    print(ed_read(fn, 3))       # prints from 3 to the end of the file: 34567890123456789

    lst = ed_find(fn, "345")
    print(lst)                  # prints [3, 13]
    print(ed_find(fn, "356"))   # prints []

    ed_replace(fn, "345", "ABCDE", 1)  # changes the file to 0123456789012ABCDE6789

    # assume we reset the file content to 01234567890123456789  (not shown)
    ed_replace(fn, "345", "ABCDE")  # changes the file to 012ABCDE6789012ABCDE6789
          
    # assume we reset the file content to 01234567890123456789 (not shown)
    # this function overwrites original content:
    ed_write(fn, ((2, "ABC"), (10, "DEFG")))   # changes file to: 01ABC56789DEFG456789

    # assume we reset the file content to 01234567890123456789 (not shown)
    ed_write(fn, ((2, "ABC"), (30, "DEFG")))  # fails. raises ValueError("invalid position 30")

    # this function overwrites original content:
    ed_write(fn, ((2, "ABC"), (10, "DEFG")))   # changes file to: 01ABC56789DEFG456789

    # assume we reset the file content to 01234567890123456789 (not shown)
    # this function inserts new text, without overwriting:
    ed_insert(fn, ((2, "ABC"), (10, "DEFG")))
    # changed file to: 01ABC23456789DEFG0123456789


