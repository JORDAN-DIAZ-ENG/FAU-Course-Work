# This program practices recursion
from turtle import *


def draw_leaf_straight(level, length):
    """ draws a leaf-like that looks like figure 1-a using the turtle module."""
    if level <= 0:
        return

    forward(length)

    backward(length * 0.6)  # go to the lower half of the line

    # Create a line to the left and reposition
    left(45)
    forward(length * 0.3)
    backward(length * 0.3)
    right(45)

    # Go to the tip of the previous line and draw the left of the leaf
    left(45)
    draw_leaf_straight(level - 1, length * 0.6)

    # Center the cursor
    right(90)

    # Draw the right of the leaf
    draw_leaf_straight(level - 1, length * 0.6)
    left(45)

    # position to the right and make a line and come back, then center
    right(45)
    forward(length * 0.3)
    backward(length * 0.3)
    left(45)

    forward(length * 0.6)  # go to the top of the first line

    draw_leaf_straight(level - 1, length * 0.6)  # draw a leaf at the tip of the top

    backward(length)


def strB(n, base=10):
    """ Converts a non-negative int value n to a string representation of n in the given base. The base parameter is
    an int between 2 and 26. For digits greater than 9 use letters 'A'-'Z' """
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return characters[n]
    else:
        return str(strB(n // base, base)) + characters[n % base]


def testif(b, testname, msgOK="", msgFailed=""):
    """ Used for unit testing"""
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b


def Cnk_m(n, k):
    """ Computing the value of the binomial coefficient using the memoization technique taught in class"""

    binomial_coefficent_cache = {}
    if (n, k) in binomial_coefficent_cache:
        return Cnk_m((n, k)[0], (n, k)[1])

    if k > n:
        result = 0
    elif k == n or k == 0:
        result = 1
    else:
        result = Cnk_m(n - 1, k - 1) + Cnk_m(n - 1, k)

    # Cache
    binomial_coefficent_cache[(n, k)] = result
    return result


def make_pairs(seq1, seq2):
    """takes as parameters two lists, seq1 and seq2, and that returns a list with all tuples (x, y) where x is in
    seq1 and y is the matching element in seq2, at the same index as x.Function make_pairs stops once it reaches the
    end of the shorter sequence. """
    if len(seq1) == 0 or len(seq2) == 0:
        return []
    return ([(seq1[0], seq2[0])]) + (make_pairs(seq1[1:], seq2[1:]))


def main():
    # Part a
    clearscreen()
    left(90)
    speed(0)
    delay(0)
    draw_leaf_straight(6, 120)
    done()

    # Part b
    print()
    print("Test for strB")

    testif(strB(123, base=16) == "7B", "Test 1")
    testif(strB(1234, base=16) == "4D2", "Test 2")
    testif(strB(123456789, base=26) == "AA44A1", "Test 3")
    testif(strB(100, base=2) == "1100100", "Test 4")

    print()
    print("Tests for Cnk_m")

    testif(Cnk_m(10, 10) == 1, "Test 5")
    testif(Cnk_m(50, 5) == 2118760, "Test 6")
    testif(Cnk_m(10, 3) == 120, "Test 7")
    testif(Cnk_m(9, 12) == 0, "Test 8")

    print()
    print("Tests for make_pairs")

    testif(make_pairs([1, 2, 3], [4, 5, 6]) == [(1, 4), (2, 5), (3, 6)], "Test 9")
    testif(make_pairs([1, 2, 3], [4, 5]) == [(1, 4), (2, 5)], "Test 10")
    testif(make_pairs([1, 2, 3], [4, 5, 6, 7, 8, 9]) == [(1, 4), (2, 5), (3, 6)], "Test 10")
    testif(make_pairs([], [4, 5, 6, 7, 8, 9]) == [], "Test 11")
    testif(make_pairs([1, 2, 3], []) == [], "Test 12")


if __name__ == "__main__":
    main()
