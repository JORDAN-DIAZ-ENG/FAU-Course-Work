#
# COP4045 Python
# Homework 3
# Do not distribute.
# Author: Ionut Cardei
#

# a)
def line_number(filein:str, fileout:str):
    """ Reads a text file with name fin and write the same text with
        line numbers prepended on each line.
        Precondition: file named filein exists and is readable and
             the user has permission to write file named fileout.
        Postconditon: file named filein was read to memory and
            the file named fileout was written to the file system.
    """
    try:
        fin = open(filein, "r")
        fout = open(fileout, "w")
 
        lineno = 1
        for line in fin:
            fout.write("{}. {}".format(lineno, line))
            lineno += 1
        fin.close()
        fout.close()
    except FileNotFoundError as exc:
        print("Error: input file {} not found.\n".format(filein))
        raise exc 
    except IOError as exc:
        print("Error: IOError while working with files {} and {}.\n".format(filein, fileout))
        raise exc 


# b)
def parse_functions(pyfilename:str):
    """Reads and parses a python code file.
       Returns a tuple with function information. Captures only top-level functions.
       This is just one way of implementing this function. We use a nested helper function for a better design.
       
       Precondition: file pyfilename exists and is readable.
       Postcondition: file pyfilename was read to memory.
    """
 
    # this is a nexted function, local to the enclosing function
    def parse_line(codeline:str, was_in_fun:bool):
        """ Parses a line of code for a ***top-level*** function definition.
            Param codeline: the line of code being parsed
            Param is_in_fun: true if the parse is in a function for this line
            Returns (in_fun, func_name): in_fun is true if the parser is in a (maybe new) function definition.
                        func_name is the name of a new fucnction that just started or
                        "" if no function has started on this line.                        
        """
        # in a function if space (' ') or newline at line start; may be reset later.
        in_fun = was_in_fun and (codeline[0] == ' ' or codeline[0] == '\n')    
        func_name = ""
        # check if a new function definition starts at the beginning of the line (index==0):
        if codeline.find("def ") == 0:
            paren_index = codeline.find("(")
            if paren_index < 0:
                printf("parse_line ERROR: wrong format for line " + codeline)
                exit(1)
            func_name = codeline[4:paren_index].strip()    # from 4 to skip "def " and with whitespace stripped
            in_fun = True
        return (in_fun, func_name)
        # NOTE: we could have used regular expressions ('re' module) but this problem is too easy for that.

    try:
        fin = open(pyfilename, "r")

        tup_lst = []             # list with resulting tuples
        fun_lst = []             # list with information on the current function
        is_in_function = False   # true if the current line belongs to a function, else false
        lineno = 0               # current line in file number
        fun_text = ""
        for line in fin:
            lineno += 1
            was_in_function = is_in_function

            (is_in_function, fn) = parse_line(line, was_in_function)
            ## debugging: print(str((is_in_function, fn)))

            if was_in_function and (fn != "" or (not is_in_function)):
                    tup_lst.append((fun_name, fun_lineno, fun_text))   # save info; new function starts now
 
            if fn != "":
                # new function definition:
                fun_text = ""
                fun_name = fn
                fun_lineno = lineno
            if is_in_function:
                fun_text += line          # add current line to function code
 
        # save info if the file ended while in function:
        if is_in_function:
                tup_lst.append((fun_name, fun_lineno, fun_text))   # save info; new function starts now
        
        fin.close()
        tup_lst.sort()            # sorting list of tuples will use the first tuple element, the function name
        return tuple(tup_lst)     # must return a tuple, not a list
    
    except FileNotFoundError as exc:
        print("Error: input file {} not found.\n".format(filein))
        raise exc 
    except IOError as exc:
        print("Error: IOError while working with files {} and {}.\n".format(filein, fileout))
        raise exc 
    


def main():
    line_number("funs.py", "out.txt")
    tups=parse_functions("funs.py")
    print(tups)
    
if __name__ == "__main__":
    main()
