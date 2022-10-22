#
# COP4045 Python
# Homework 6
# Do not distribute.
# Author: Ionut Cardei


import turtle
import random
import testif
import itertools


## a) execute run_draw_leaf or run_draw_leaf_straight from the Python
## console in Spyder or idle.

def run_draw_leaf():
    turtle.clearscreen()
    turtle.up()
    turtle.goto(0, -400)
    turtle.delay(0)
    turtle.down()
    turtle.left(90)   # growing top->down
    draw_leaf(7, 120)

def run_draw_leaf_straight():
    turtle.clearscreen()
    turtle.up()
    turtle.goto(0, -400)
    turtle.delay(0)
    turtle.down()
    turtle.left(90)   # growing top->down
    draw_leaf_straight(6, 120)


def draw_leaf(depth, length, scale1=0.3, scale2=1.5, scale3=0.4, alpha=45, beta=60):
    if depth == 0:
        return
    turtle.forward(length)      # trunk
    turtle.left(alpha)          # start left branch
    turtle.forward(length * scale1)
    draw_leaf(depth - 1, scale3 * length, scale1, scale2, scale3, alpha, beta)
    turtle.up()
    turtle.backward(length * scale1)    # back to split point
    
    turtle.right(beta)         # back on trunk direction, 
    turtle.down()               
    turtle.forward(length * scale2)      # middle branch

    # center sub-leaf:
    draw_leaf(depth - 1, scale3 * length * scale2, scale1, scale2, scale3, alpha, beta)
    turtle.up()
    turtle.backward(length * scale2)    # back to split point

    # right branch:
    turtle.right(alpha)
    turtle.down()
    turtle.forward(length * scale1)
    # right sub-leaf:
    draw_leaf(depth - 1, scale3 * length, scale1, scale2, scale3, beta, alpha)

    # back from right branch:
    turtle.up()
    turtle.backward(length * scale1)
    turtle.left(beta)
    # now at split point
    turtle.backward(length)
    turtle.down()
    
    
    

def draw_leaf_straight(depth, length, scale1=0.3, scale2=1.5, scale3=0.4, alpha=45, beta=50):
    if depth == 0:
        return
    turtle.forward(length)      # trunk
    turtle.left(alpha)          # start left branch
    turtle.forward(length * scale1)
    draw_leaf_straight(depth - 1, scale3 * length, scale1, scale2, scale3, alpha, beta)
    turtle.up()
    turtle.backward(length * scale1)    # back to split point
    
    turtle.right(alpha)         # back on trunk direction, 
    turtle.down()               
    turtle.forward(length * scale2)      # middle branch

    # center sub-leaf:
    draw_leaf_straight(depth - 1, scale3 * length * scale2, scale1, scale2, scale3, alpha, beta)
    turtle.up()
    turtle.backward(length * scale2)    # back to split point

    # right branch:
    turtle.right(beta)
    turtle.down()
    turtle.forward(length * scale1)
    # right sub-leaf:
    draw_leaf_straight(depth - 1, scale3 * length, scale1, scale2, scale3, alpha, beta)

    # back from right branch:
    turtle.up()
    turtle.backward(length * scale1)
    turtle.left(beta)
    # now at split point
    turtle.backward(length)
    turtle.down()

# ----------------------------------------------------------


def base10(n):
    return [] if n == 0 else [n % 10] + [base13(n // 10)]

def str10(n):
    if n == 0:
        return ""
    return str10(n // 10) + str(n % 10)


## b)

def strB(n, base=10):
    digits = "0123456789" + "".join([chr(ord('A') + i) for i in range(26)])
    def __strB(m):
        if m == 0:
            return ""
        return __strB(m // base) + digits[m % base]
    return '0' if n == 0 else __strB(n)


def test_strB():
    testif.testif(strB(123456789, base=26) == "AA44A1", "strB_26")
    testif.testif(strB(1234, base=16) == "4D2", "strB_16")
    testif.testif(strB(100, 2) == '1100100', "strB_2")
    
                       
## c)
# no memoization: O(2^n)
def Cnk(n, k):
    if k == 0 or k == n:
        return 1
    return Cnk(n-1, k-1) + Cnk(n-1, k)
        

cache_Cnk = dict()

def Cnk_m(n, k):    
    def aux(nn, kk):
        if (nn, kk) in cache_Cnk:
            return cache_Cnk[(nn,kk)]

        if kk == 0 or kk == nn:
            val = 1
        else:
            val = aux(nn-1, kk-1) + aux(nn-1, kk)
        cache_Cnk[(nn,kk)] = val
        return val

    return aux(n, k)

def test_Cnk():
    testif.testif(Cnk_m(100, 1) == 100, "Cnk_m(100, 1)")
    testif.testif(Cnk_m(100, 100) == 1, "Cnk_m(100, 100)")
    testif.testif(Cnk_m(100, 0) == 1, "Cnk_m(100, 0")
    testif.testif(Cnk_m(20, 10) == 184756, "Cnk_m(20, 10)")
    testif.testif(Cnk_m(100, 50) == 100891344545564193334812497256, "Cnk_m(100, 50)")
    testif.testif(Cnk_m(10, 3) == 120, "Cnk_m(10, 3)")
    

## d)

def make_pairs(seq1, seq2, index=0, acc=[]):
    if index >= len(seq1) or index >= len(seq2):
        return acc
    return make_pairs(seq1, seq2, index + 1, acc + [(seq1[index], seq2[index])])


# demo:
print(make_pairs([1,2,3], [4,5,6,7,8,9]))

#=========================================================================

