# This program is used to test out functional programming in python
import itertools


def rnd_gen(x0, n):
    """ Generates a sequence of random ints"""
    if n >= 0:
        for i in range(0, n):
            x0 = (22695477 * x0 + 1) % 2 ** 32
            yield x0
    else:
        while True:
            x0 = (22695477 * x0 + 1) % 2 ** 32
            yield x0


def gen_rndtup(m):
    """ Creates an infinite sequence of tuples (a, b) where a and b are
two random integers obtained using the rnd_gen(1, -1) generator from Problem 2 and 0 ≤ a ≤ b < m."""

    rand_num = rnd_gen(1, -1)
    while True:
        a = next(rand_num) % m
        b = next(rand_num) % m
        if a < b:
            yield a, b


def main():
    """ Main Driver Function"""
    # Part A Code
    print("Part A:")
    tuples = gen_rndtup(10)
    final = itertools.islice(tuples, 0, 10)
    for element in final:
        print(element)

    print()

    # Part B Code
    print("Part B:")
    ans = itertools.islice(itertools.filterfalse(lambda x: x[0] + x[1] < 6, gen_rndtup(10)), 0, 8)
    it = iter(ans)
    for element in it:
        print(element)

    print()

    # Part C Code
    print("Part C:")
    ans = itertools.islice((res for res in zip(rnd_gen(1, -1), rnd_gen(2, -1)) if (res[0] % 101) < res[1] % 100), 0, 8)
    for element in ans:
        print((element[0] % 101, element[1] % 100))

    print()

    # Part D Code
    print("Part D:")
    ans = rnd_gen(1, -1)
    elements_less_than_100 = map(lambda x: x % 100, ans)
    elements_divisible_by_13 = filter(lambda x: x % 13 == 0, elements_less_than_100)
    final_lst = itertools.islice(elements_divisible_by_13, 0, 10)
    for element in final_lst:
        print(element)

    print()

    # Part E Code
    print("Part E:")
    ans = gen_rndtup(10)
    elements_that_total_5 = filter(lambda x: (x[0] + x[1]) >= 5, ans)
    final_lst = itertools.islice(elements_that_total_5, 0, 10)
    for element in final_lst:
        print(element)


if __name__ == "__main__":
    main()
