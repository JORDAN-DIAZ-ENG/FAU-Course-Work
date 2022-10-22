#
# COP4045 Python
# Homework 5
# Do not distribute.
# Author: Ionut Cardei

import random
import itertools
import functools


class RndSeq:
    m = 2**32
    a = 22695477
    c = 1
    def __init__(self, x0=0, n=100):
        self.x = x0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n != 0:
            self.x = (RndSeq.a * self.x + RndSeq.c) % RndSeq.m
            if self.n > 0:
                self.n -= 1
            return self.x
        raise StopIteration


def rnd_gen(x0, n=100):
    m = 2**32
    a = 22695477
    c = 1
    x = x0
    while n > 0 or n < 0:
        x = (a * x + c) % m
        yield x
        n = n - 1


def main_problem1():
    print(iter(RndSeq(2, 10)))
    print(list(rnd_gen(2, 10)))
    

