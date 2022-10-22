#
# COP4045 Python
# Homework 5
# Do not distribute.
# Author: Ionut Cardei

import random
import itertools
import functools

from p1 import rnd_gen

# a)
def gen_rndtup(m):
    rndgen = rnd_gen(1, -1)
    while True:
        b = next(rndgen) % m
        a = next(rndgen) % (b + 1)
        yield (a, b)


# b)

n = 8
m = 10
p = 6
print("b): {} random tuples (a,b) with a+b>={} using lambda and filter:".format(n,p))

for tup in itertools.islice(itertools.filterfalse(lambda t: t[0]+t[1] < p, gen_rndtup(m)), n):
    print(tup)
        

# c)


# gen is equivalent to gen_rndtup
# itertools.repeat(0) goes on forever

print("\nc): {} random tuples (a,b) with 0<=a<=b<=100 using zip:".format(n))

# split up for readability:
for t in itertools.islice(                   # get n=8 tuples (a,b)...
            filter(
                lambda tup: tup[0] <= tup[1],      # that have a<b
                zip(                               # from a stream of tuples that spring from...
                    map(lambda a: a % 101, rnd_gen(1, -1)),       # random sequence between 0 and 100
                    map(lambda a: a % 101, rnd_gen(2, -1))
                    )
                ),
            n): 
    print(t)


# d)
print("\nd): the first 10 random numbers between 0 and 100 that are divisible to 13:")
for x in itertools.islice(
            filter(
                lambda y: y % 13 == 0,
                map(
                    lambda z: z % 101,
                    rnd_gen(1, -1)
                    )
                ),
            10):
    print(x)

# e)

# the stream of random tuples with the required property:
seq1 = filter(lambda tup: tup[0]+tup[1] >= 5, gen_rndtup(101))

# the stream of the first 10 tuples:
seq2 = itertools.islice(seq1, 10)

tup_sum = functools.reduce(lambda s, tup: (s[0]+tup[0], s[1]+tup[1]), seq2)

print("\ne): Tuple stream sum =", tup_sum)

