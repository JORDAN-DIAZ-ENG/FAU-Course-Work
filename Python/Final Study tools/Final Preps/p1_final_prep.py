"""
a) Write a function seq_save(filename, seq) that writes a sequence
(e.g. list) of strings seq to a file so that it is possible to recover
later the original sequence. The same strings and in the correct order.
The challenge is that strings may contain \n, so we can't use \n as
n element separator.

sequence example: list of strings = ["abc", "0", "de"]
"""


def seq_save(filename, seq):
    with open(filename, "w") as f:
        for s in seq:
            f.write(str(len(s)) + "\n")
            f.write(s)


def seq_read(filename):
    """Read a sequence of strings from a text file back to a list of strings.
    """
    with open(filename, "r") as f:
        lst = []
        sz = 0
        while sz >= 0:
            sz = -1
            line = f.readline()
            if len(line) > 0:
                sz = int(line.strip())
                s = f.read(sz)
                lst.append(s)
        return lst

def seq_read_nth(filename, idx):
    """Read the string with index idx from the file.
    Returns "" if not 0<=idx<sequence length.
    """
    ret = ""
    if idx < 0:
        return ""
    with open(filename, "r") as f:
        lst = []
        while True:
            line = f.readline()
            if len(line) > 0:
                sz = int(line.strip())
                if idx == 0:
                    return f.read(sz)
                else:
                    f.seek(f.tell() + sz)
                    idx -= 1
            else:
                return ""


def test_seq_io():
    fn = "seq-test.txt"
    lst1 = ["abc", "0", "123\n\n567", "89", "", "", "z"]
    seq_save(fn, lst1)
    lst2 = seq_read(fn)
    testif(lst1 == lst2, "seq write and read")
    for n in range(len(lst1)):
        testif(lst1[n] == seq_read_nth(fn, n), "seq_read_nth: n={}".format(n))

    n = -1
    testif("" == seq_read_nth(fn, n), "seq_read_nth: n={}".format(n))
    n = len(lst1)
    testif("" == seq_read_nth(fn, n), "seq_read_nth: n={}".format(n))


test_seq_io()