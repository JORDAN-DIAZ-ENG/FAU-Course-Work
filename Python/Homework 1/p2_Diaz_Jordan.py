# Jordan Diaz
# This program computes all possible pythagorean triples (a, b, c)
# This is similar to an assignment I did in discrete math
# I learned that (n, n, n) = n^3 possibilities where each available position is another for loop
# If there were quadruples instead of triples there would be 4 for loops

def find_pythagorean(n):
    """This Function will go through every possibility of a, b, c and return a list of triples"""

    triples_list = []

    for i in range(1, n + 1):  # n^1
        for j in range(1, n + 1):  # n^2
            for k in range(1, n + 1):  # n^3
                if ((i ** 2) + (j ** 2)) == k ** 2:
                    triple = (i, j, k)
                    triples_list.insert(triples_list.count(0), triple)
    triples_list.reverse()
    return triples_list


for triples in find_pythagorean(int(input("Please Enter a positive Integer: "))):
    print(triples)
