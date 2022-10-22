# This program experiments with classes in python
class NVector(object):
    def __init__(self, *sequence):
        """ Constructor, creates a list of elements in the sequence"""
        self.elements_of_sequence = []
        if len(sequence) == 1:
            for iterable in sequence:
                for index in iterable:
                    self.elements_of_sequence.append(index)
        elif len(sequence) > 1:
            for element in sequence:
                self.elements_of_sequence.append(element)

    def __len__(self):
        """ Returns the length of the list from the elements in the sequence"""
        return len(self.elements_of_sequence)

    def __getitem__(self, index):
        """ Returns the index from the list of elements in the sequence"""
        return self.elements_of_sequence[index]

    def __setitem__(self, index, value):
        """ Modifies the value at an index from the list of elements in the sequence"""
        self.elements_of_sequence[index] = value

    def __str__(self):
        return str(self.elements_of_sequence)

    def __eq__(self, other):
        if type(other) == NVector:
            if self.elements_of_sequence == other.elements_of_sequence:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if type(other) == NVector:
            if self.elements_of_sequence != other.elements_of_sequence:
                return True
            else:
                return False
        else:
            return True

    def __add__(self, other):
        """ Adds NVector or number if it is the right of it"""
        temp_list = []
        if type(other) == NVector:
            list_a = []
            list_b = []

            for items in self.elements_of_sequence:
                list_a.append(items)
            for items in other.elements_of_sequence:
                list_b.append(items)

            if len(list_a) > len(list_b):
                for i in range(0, abs(len(list_a) - len(list_b))):
                    list_b.append(0)
            elif len(list_a) < len(list_b):
                for j in range(0, abs(len(list_a) - len(list_b))):
                    list_a.append(0)

            for k in range(0, len(list_a)):
                temp_list.append(list_a[k] + list_b[k])

        elif type(other) == int or type(other) == float:
            for element in self.elements_of_sequence:
                temp_list.append(other + element)

        return NVector(temp_list)

    def __radd__(self, other):
        """ Adds a number if it is the the Left of it to each element of the sequence, must be number"""
        temp_list = []
        if type(other) == int or type(other) == float:
            for element in self.elements_of_sequence:
                temp_list.append(other + element)
            return NVector(temp_list)

    def __mul__(self, other):
        """ multiplies NVector of numbers or number if it is the right of it, NVectors must be same size"""
        temp_value = 0
        if type(other) == NVector:
            for i in range(0, len(self.elements_of_sequence)):
                temp_value += self.elements_of_sequence[i] * other[i]
        elif type(other) == int or type(other) == float:
            for j in range(0, len(self.elements_of_sequence)):
                temp_value += self.elements_of_sequence[j] * other
        return temp_value

    def __rmul__(self, other):
        """ multiplies a number if it is the the Left of it to each element of the sequence, must be number"""
        temp_value = 0
        if type(other) == int or type(other) == float:
            for j in range(0, len(self.elements_of_sequence)):
                temp_value += self.elements_of_sequence[j] * other
        return temp_value

    def zeros(self, n):
        """ returns a new NVector object with dimension n with all elements 0"""
        temp_list = []
        for i in range(0, n):
            temp_list.append(0)
        return NVector(temp_list)


def testif(b, testname, msgOK="", msgFailed=""):
    """ Unit Testing"""
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b


def main():
    """ used for testing of the NVector class"""
    # testing part __init__, __eq__, __ne__, __setitem__
    a1 = NVector([3, 0, 1, -1])
    a2 = NVector(3, 0, 1, -1)
    testif(a1 == a2, "__init__, __eq__", "constructor works and eq works", "constructor works or eq failed")
    a2[1] = 10
    testif(a2[1] == 10 and a1 != a2, "__setitem__, __ne__", "setitem works and ne works", "setitem or ne failed")

    # testing part __len__, __getitem__
    testif(a1.__len__() == 4 and a1.__getitem__(0) == 3, "__len__, __getitem__", "these worked", "these failed")

    # testing __str__
    testif(type(a1.__str__()) == str, "__str__", "worked", "failed")

    # testing __add__ , __radd__
    b1 = NVector(3, 0, 1, -1)
    b2 = NVector(1, 2, 3, 4)
    expected = [4, 2, 4, 3]
    testif((b1 + b2).elements_of_sequence == expected and b1 + 10 == 10 + b1, "__add__, __radd__", "worked", "failed")

    # testing __mul__ and __rmul__
    testif(b1 * b2 == 2 and b1 * 10 == 30 and 10 * b1 == 30, "__mul__, __rmul__", "worked", "failed")


if __name__ == "__main__":
    main()
