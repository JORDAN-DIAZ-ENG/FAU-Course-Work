def flatten(lst):
    locall = []
    for x in lst:
        if type(x) != list and type(x) != tuple:
            locall.append(x)
        else:
            locall.extend(flatten(x))
    return locall