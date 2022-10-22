def print_flatten(lst):
    for x in lst:
        if type(x) != list and type(x) != tuple:
            print(x, end=" ")
        else:
            print_flatten(x)