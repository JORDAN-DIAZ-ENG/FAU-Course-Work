# This program tests random number generation using iterators and generators

class RndSeq(object):
    """ Class uses the linear congruential generator to generate a sequence of random ints"""
    def __init__(self, x0, n):
        self.m = 2 ** 32
        self.a = 22695477
        self.c = 1
        self.n = n
        self.x0 = x0
        self.loop_forever = False

        if self.n < 0:
            self.loop_forever = True

    def __iter__(self):
        """ Iterator"""
        return self

    def __next__(self):
        """ Returns the next iteration"""
        if self.loop_forever:
            self.x0 = (self.a * self.x0 + self.c) % self.m
            return self.x0
        else:
            if self.n == 0:
                raise StopIteration
            self.x0 = (self.a * self.x0 + self.c) % self.m
            self.n -= 1
            return self.x0


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


def main():
    """ Driver function"""
    rnd = RndSeq(1, 10)
    print([i for i in rnd])

    print(list(rnd_gen(1, 3)))


if __name__ == "__main__":
    main()
