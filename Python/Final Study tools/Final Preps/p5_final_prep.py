# version that passes the accumulated list in the second param ll
def flatten_pure(lst):
    """Returns  flat list with all elements (non-list/non-tuple) from lst."""
    def flatten_pure_aux(lst, ll):
        if lst == []:
            return ll
        if type(lst[0]) != list and type(lst[0]) != tuple:
            # not a collection:
            return flatten_pure_aux(lst[1:], ll + [lst[0]])
        return flatten_pure_aux(lst[1:], ll + flatten_pure(lst[0]))
    return flatten_pure_aux(lst, [])
# version that does not rely on a second parameter:
def flatten_pure2(lst):
    """Returns  flat list with all elements (non-list/non-tuple) from lst."""
    if lst == []:
        return []
    if type(lst[0]) != list and type(lst[0]) != tuple:
        # not a list/tuple:
        return [lst[0]] + flatten_pure2(lst[1:])
    # lst[0] is a nested list or tuple:
    return flatten_pure2(lst[0]) + flatten_pure2(lst[1:])
demolst = [[0,1],2,[3,[4,[5],6],7,[8,[9,10]]],11]
print_flatten(demolst)
print()
print(flatten(demolst))
print(flatten_pure(demolst))
print(flatten_pure2(demolst))