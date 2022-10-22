# Jordan Diaz
# This Program finds duplicate substring and max duplicate substring
# Cannot use str functions

def find_dup_str(s, n):
    """ This Function returns the first occurring substring of length n (if any) """

    if n >= len(s) or n < 1:
        return ""

    for i in range(0, len(s) - 1):
        curr_str = s[i: i + n]

        for k in range(i + 1, len(s) - 1):
            next_str = s[k:k + n]

            if curr_str == next_str:
                return curr_str
    return ""


def find_max_dup(s):
    """ This Function returns the largest duplicate substring"""
    curr_str = ""
    n = len(s) // 2

    while curr_str == "":
        curr_str = find_dup_str(s, n)
        n -= 1

        if n <= 0:
            break

    return curr_str


print(find_dup_str(input("Type a string to find first substring: "), int(input("Type the length of the substring: "))))
print(find_max_dup(input("Type a string to find max substrings: ")))
