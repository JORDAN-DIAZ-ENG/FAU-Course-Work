# Python Programming.
# Homework 2, problem 3
# Instructor: Dr. Ionut Cardei
# Do not distribute.

import pylab
import math


def plot_function(fun_str, domain, ns):
    # print table header:
    print("{:>10}{:>10}".format("x", "y"))
    print("-" * 20)      

    (xmin, xmax) = domain
    xs = []   # do NOT write xs = ys = []. That makes xs and ys point to the same list object.
    ys = []
    dx = (xmax - xmin) / (ns - 1)

    i = 0
    for i in range(0, ns):
        x = xmin + i * dx
        xs.append(x)
        y = eval(fun_str)
        ys.append(y)

        print("{0:>+10.4f}{1:>+10.4f}".format(x, y))

    pylab.plot(xs, ys, "bo-")
    pylab.xlabel('x')
    pylab.ylabel("y")
    pylab.title(fun_str)
    pylab.show()


#fun_str = "2 * math.sin(2*math.pi * x)"
fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

plot_function(fun_str, (xmin, xmax), ns)
