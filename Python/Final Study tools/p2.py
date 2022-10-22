import itertools
import functools


# part a
def cartesian2(s1: list, s2: list):
    """yields sequence of tuples from x1 and x2 """
    return [list(zip(values, s1)) for values in itertools.permutations(s2, len(s1))]


a = [0, 1]
b = ["a", "b", "c"]
print(cartesian2(a, b))


