# Python Programming.
# Homework 1, problem 2
# Instructor: Dr. Ionut Cardei
# Do not distribute.

import math

n_str = input("Enter n: ")
# assume this represents an int number
n = int(n_str)    # ... so this expression succeeds.

if (n < 0):
    print("Error: n must be positive integer")
    exit(1)

for a in range(1, n+1):
    bmax = int(math.sqrt(n**2 - a**2))
    for b in range(1, bmax + 1):
        hyp_sq = a**2 + b**2
        c_float = math.sqrt(hyp_sq)

        # if c is an int (a whole number):
        if c_float == int(math.sqrt(hyp_sq)):
            # no need to check for c<=n since b is limited
            c = int(c_float)
            print(a, b, c)

