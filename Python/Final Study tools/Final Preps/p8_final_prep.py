def enumerate_seq(seq):
    i = 0
    for x in seq:
        yield (i, x)
        i = i + 1
for tup in enumerate_seq(["abc", 10, "def"]):
    print(tup)