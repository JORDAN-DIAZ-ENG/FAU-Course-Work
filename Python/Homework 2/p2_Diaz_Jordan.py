# Jordan Diaz, This program teaches a handful of python concepts
def concatenate(separator_char, *strings):
    """ This program concatenates multiples strings separated by a specific character"""
    temp_str = ""
    for i in range(0, len(strings)):
        if i != len(strings) - 1:
            temp_str += strings[i] + separator_char
        elif i == len(strings) - 1:
            temp_str += strings[i]
    return temp_str


# Pythagorean Triples
pythagorean_triples = [(i, j, k) for i in range(1, 100 + 1) for j in range(1, 100 + 1) for k in range(1, 100 + 1) if
                       ((i ** 2) + (j ** 2)) == (k ** 2)]

print(pythagorean_triples)

# list of strings in a tuple
lst = ["one", "seven", "three", "two", "tem"]

lst_of_strings = [(len(elements), elements.capitalize()) for elements in lst if len(elements) > 3]

print(lst_of_strings)

# Reorder Names
lst = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]

final_lst = ["{}, {}".format(new_elements[1], new_elements[0]) for new_elements in
             [elements.split() for elements in lst]]
print(final_lst)

print(concatenate(": ", "one", "two", "three"))
print(concatenate(" and ", "bonny", "Clyde"))
print(concatenate(" and ", "single"))
