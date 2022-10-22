def gen_diff(seq):
    it = iter(seq)
    x = next(it)
    for y in it:
        yield y - x
        x = y
seq = [2,-1,5,4,3,6,4,-3,0,5,7]
odds = filter(lambda x: x%2!=0, seq)
squares_odds = map(lambda y: y*y, odds)
differences = gen_diff(squares_odds)
m = functools.reduce(max, differences)
print("Max difference between successive squares of odd numbers:",m)
#in one expression:
m = functools.reduce(max, gen_diff(map(lambda y: y*y,
                                       filter(lambda x: x%2!=0, seq))))
print("Max difference between successive squares of odd numbers from seq:",m)