#
# COP4045 Python
# Homework 3
# Do not distribute.
# Author: Ionut Cardei
#

from math import sqrt

# a)

N = 100
# naive version O(N^3):
pythagoras_naive = [(a, b, c) for a in range(1, 1 + N) for b in range(1, 1 + N)
              for c in range(1, 1 + N) if c * c == a * a + b * b]

# faster version, O(N^2):
pythagoras = [(a, b, int(c_float)) for a in range(1, N - 1)
              for b in range(1, 1 + int(sqrt(N*N - a*a))) for c_float in [sqrt(a*a + b*b)]
              if c_float == int(c_float)]
# the last 'for' is for giving c_float a value


# check that we got all tuples:  should  print []
print("Should be []: " + str([ t for t in pythagoras_naive if t not in pythagoras]))


# b)
ls = ['one', 'seven', 'three', 'two', 'ten']
tuples = [(len(s), s.upper()) for s in ls if len(s) > 3]      


# c)
names =  ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
fullnames = [ nm[1] + ", " + nm[0] for nm in [fullname.split() for fullname in names]]


# d)
def concatenate(sep:str, *args):
    # the shortest version is this:
    return sep.join(args)

print(concatenate(' and ', "one", "two", "three"))
