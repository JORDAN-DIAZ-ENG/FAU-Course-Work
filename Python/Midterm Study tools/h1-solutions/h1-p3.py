# Python Programming.
# Homework 2, problem 3
# Instructor: Dr. Ionut Cardei
# Do not distribute.

# part a)

def find_dup(s, n):
    foundss = ""
    # index i marks the start of the substring to look for
    i = 0
    while i <= len(s) - 2*n and foundss == "":
        j = i + n
        while j <= len(s) - n and foundss == "":
            # compare up to n chars from index i with  k chars from index j: 
            k = 0
            while k < n and s[i + k] == s[j + k]:
                k = k + 1
            # did we find all n characters equal ?
            if k == n:
                foundss =  s[i:i+n]    # slice with substring of length n to return
            j = j + 1
        i = i + 1
    return foundss



def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing. 
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b



# part b)

# main program:

s = input("Enter string: ")
n = int(input("Enter n: "))
print("Found substring of length {}: '{}'".format(n, find_dup(s, n)))

# more testing:
s1 = "abCDEfCDEghi"
testif(find_dup(s1, 1) == "C", "find 1")
testif(find_dup(s1, 2) == "CD", "find 2")
testif(find_dup(s1, 3) == "CDE", "find 3")
for i in range(4, len(s1)+4):
    testif(find_dup(s1, i) == "", "find " + str(i))

# test boundary case:
testif(find_dup("123456734567", 5) == "34567", "find 5, boundary case")


s2 = "0123456789"
testif(find_dup(s2, 1) == "", "not found 1")
testif(find_dup(s2, 2) == "", "not found 2")
testif(find_dup(s2, 6) == "", "not found 6")

testif(find_dup("", 1) == "", "not found '' 1")
testif(find_dup("", 2) == "", "not found '' 2")
testif(find_dup("", 6) == "", "not found '' 6")


# part c)

# Algorithm for find_max_dup:

# function find_max_dup(s)
# 1.  maxss = ""
# 2.  for n=len(s) / 2; n>=1 and maxss==""; n--
# 2.1   maxss = find_dup(s, n)
# 3.   return maxss


# part d)
def find_max_dup(s):
    n = len(s) // 2
    maxss = ""
    while n >= 1 and maxss == "":
        maxss = find_dup(s, n)
        n = n - 1
    return maxss


s = input("Enter string: ")
maxss = find_max_dup(s)
print("Found maximal duplicated substring '{}' of length {}".format(maxss, len(maxss)))


# more testing:
testif(find_max_dup(s1) == "CDE", "find_max_dup s1")
testif(find_max_dup(s2) == "", "find_max_dup s2")

