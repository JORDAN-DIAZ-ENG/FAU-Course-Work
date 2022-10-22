def cycle_seq(seq):
    """Cycles through all elements from iterable seq."""
    lst = [x for x in seq]
    while True:
        for i in lst:
            yield i
# uncomment for infinite cycling:
#for i in cycle_seq((3,4,5)):
#    print(i, end=" ")