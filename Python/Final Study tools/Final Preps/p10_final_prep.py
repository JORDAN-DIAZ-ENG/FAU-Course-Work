# no change:
def gen_diff(seq):
    """Generate sequence with the differences between adjacent elements in seq.
    If seq has less then two elements then it generates the empty sequence.
    Check out with list(gen_diff([1]))"""
    it = iter(seq)
    x = next(it)
    for y in it:
        yield y - x
        x = y
seq = [2,-1,5,4,3,6,4,-3,0,5,7]
odds = (i for i in seq if i%2!=0)
squares_odds = (i*i for i in odds)
differences = gen_diff(squares_odds)
m = -1
for x in differences:
    if x < m:
        m = x
# or just:
#  m = max(differences)
# in one expression:
m = max(gen_diff(i*i for i in seq if i % 2!=0))  # beautiful!
print("Max difference between successive squares of odd numbers from seq:",m)