# Jordan Diaz
# This program will plot any function evaluated from the terminal with a table
import math
import matplotlib.pyplot as plotter


def plot_function(fun_str, domain, points, style):
    """ Function plots a given function"""

    xs = []
    ys = []
    # prepare the domain for the function we graph
    x = domain[0]
    difference = (domain[1] - domain[0]) / points

    while x <= domain[1]:
        xs.append(x)
        x += difference

    for x in xs:
        y = eval(fun_str)
        ys.append(y)

    plotter.plot(xs, ys, style)
    plotter.xlabel("x - axis")
    plotter.ylabel("y - axis")
    plotter.title(fun_str)
    plotter.show()
    print("{:>7s}     {:>10s} ".format("x", "y"))
    print("---------------------------")
    for x in xs:
        y = eval(fun_str)
        print("{:10.4f}     {:10.4f} ".format(x, y))


plot_function(input("Enter a function with variable x: "),
              (float(input("Enter x-min: ")), float(input("Enter x-max: "))),
              int(input("Enter number of samples: ")),
              "rx-")
