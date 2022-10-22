def decimate(n, seq):
    """Yield each nth elements from sequence.
    """
    i = 0
    for x in seq:
        if i % n == 0:
            yield x
        i += 1


print("Decimation by 3 and by 4: ", tuple(decimate(4, decimate(3, range(100)))))