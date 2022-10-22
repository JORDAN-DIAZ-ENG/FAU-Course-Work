# Jordan Diaz
# This Program solves quadratic equations and graphs them
import math
import matplotlib.pyplot as plt


def plot_quadratic(var_a, var_b, var_c, domain_min, domain_max, points, style):
    """ Function plots a quadratic function, needs a, b, c, min x, max x, number of points, and style"""

    xs = []
    ys = []
    # prepare the domain for the function we graph
    x = domain_min
    difference = (domain_max - domain_min) / points

    while x <= domain_max:
        xs.append(x)

        y = (var_a * x ** 2) + (var_b * x) + var_c

        ys.append(y)
        x += difference

    plt.plot(xs, ys, style)
    plt.show()


while True:
    a = input("type the value of a: ")

    if a == "":
        break
    a = float(a)

    b = float(input("type the value of b: "))
    c = float(input("type the value of c: "))

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant < 0:
        print("no real solutions")
        plot_quadratic(a, b, c, (-b / (2 * a)), 4, 150, "rx-")
    elif discriminant == 0:
        x1 = x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print("one solution: ", x1)
        plot_quadratic(a, b, c, x1 - 2, x2 + 2, 150, "rx-")
    elif discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print("two solutions: {} and {}".format(x1, x2))
        plot_quadratic(a, b, c, x1 - 2, x2 + 2, 150, "rx-")

    print()
