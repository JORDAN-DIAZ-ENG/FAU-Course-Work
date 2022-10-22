def scan(fun, initial, seq):
    """Generates the sequence of accumulated results of applying the
    func function on the current running result the next element from seq.
    """
    s = initial
    yield s
    for x in seq:
        s = fun(s, x)
        yield s


# a)
# print the sequence of partial sums in range(0,10):
print(tuple(scan(lambda x, y: x + y, 0, range(10))))
# b)
# compute the partial concatenations of a sequence of lists:
tuple(scan(lambda a, b: a + b, [], ([0, 1], [2], [3, 4, 5], [6], [7, 8, 9])))