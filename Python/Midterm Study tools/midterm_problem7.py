# Written by Jordan Diaz for python class midterm


class ClosedInterval(object):
    """ Implements a closed interval [a,b] = {x|a<=x<=b and a,b element of all real numbers, a <= b} on the real
    number line} """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def min(self):
        """ returns the lower bound of the closed interval"""
        return self.b

    def max(self):
        """ returns the upper bound of the closed interval"""
        return self.a

    def __contains__(self, item):
        """used by operator in, returns True if the parameter x belongs to the closed interval [a, b]"""
        if self.a <= item <= self.b:
            return True
        else:
            return False

    def __mul__(self, other):
        """used by operator * to return the closed interval that contains both self and another interval object given
        as parameter """
        new_a = self.a
        new_b = self.b
        if other.a < self.a:
            new_a = other.a
        if other.b > self.b:
            new_b = other.b
        return [new_a, new_b]

    def __add__(self, other):
        """used by the addition operator + to return a new interval that is self shifted by the number given as
        parameter """
        return [self.a + other, self.b + other]

    def __radd__(self, other):
        """ the reflected addition operator"""
        return [self.a + other, self.b + other]

    def __str__(self):
        """return a string representation of the closed interval"""
        return str([self.a, self.b])

    def __repr__(self):
        """return a string representation of the closed interval"""
        return str([self.a, self.b])


i1 = ClosedInterval(2, 5)
print(i1)
print(0 in i1)
print(3.5 in i1)

i2 = ClosedInterval(1, 6)
print(i1 * i2)

i3 = ClosedInterval(1, 3.5)
print(i1 * i3)

i4 = ClosedInterval(3, 4)
print(i1 * i4)

i5 = i1 + 10
print(i5)

i6 = 20 + i1
print(i6)
