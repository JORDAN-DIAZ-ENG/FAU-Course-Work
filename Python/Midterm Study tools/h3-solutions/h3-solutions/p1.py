# Python Programming.
# Homework 3, problem 1
# Instructor: Dr. Ionut Cardei
# Do not distribute.


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



class NVector:
    """ Class that implements an n-dimensional real vector.
    """
    
    def __init__(self, *args):
        """ Constructor with a variable number of arguments.
            NVector(1,2,3) and NVector([1,2,3]) produce the same result.
        """
           
        if len(args) == 1:
            self.__data = list(args[0])    # e.g. NVector([1,2,3,4])
        elif len(args) > 1:
            self.__data = list(args)       # e.g. NVector(3,4,5)
        else:
            raise ValueError(__name__ + " ERROR: argument missing.")
        self.dim = len(self.__data)

    def __len__(self):
        """ Returns the vector's dimension.
        """
        return self.dim

    def __getitem__(self, index):
        """ Indexing operator. Supports negative indexes.
            Throws IndexError if index is invalid.
        """
        # next statement may throw IndexError if the index is wrong
        return self.__data[index]


    def __setitem__(self, index, val):
        """ Indexed assignment   operator []. self[index] is assigned value val.
            Supports negative indexes.
            Throws IndexError if index is invalid.
        """
        # next statement may throw IndexError if the index is wrong
        self.__data[index] = val


    def __str__(self):
        """ Return a pretty-printable string representation for the object.
        """
        return str(self.__data)


    def __repr__(self):
        """ Return an unambiguous string representation for the object.
        """
        return str(self)

    def __eq__(self, other):
        """ Equalty operator.
        """
        return self.__data == other.__data

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        """ Addition operator.
            Other can be another NVector or a number.
        """
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("{} Error: wrong vector length {}".format(__name__, len(other)))
            return NVector([self.__data[i] + other.__data[i] for i in range(len(self))])
        else:
            # other must be a number:
            return NVector([self.__data[i] + other for i in range(len(self))])

    def __radd__(self, other):
        """ Reflected addition operator.
        """
        return self + other


    def __mul__(self, other):
        """ Multiplication operator. Returns the scalar product.
            Other can be another NVector or a number.
        """
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("{} Error: wrong vector length {}".format(__name__, len(other)))
            scalar_prod = 0.0
            for i in range(len(self)):
                scalar_prod += self.__data[i] * other.__data[i]
            return scalar_prod
        else:
            # other must be a number:
            scalar_prod = 0.0
            for i in range(len(self)):
                scalar_prod += self.__data[i] * other
            return scalar_prod

    def __rmul__(self, other):
        """ Reflected multiplication operator.
        """
        return self * other

    def zeros(n):
        """ Returns an NVector with n zeros.
        """
        return NVector([0] * n)


def main():
    """ unit tests
    """
    v0 = NVector(0,1,2,3,4,5)
    testif(v0[3] == 3, "getitem 1") 
    v1 = NVector([0,1,2,3,4,5])
    testif(v1[3] == 3, "getitem 2")
    testif(v1[-3] == 3, "getitem negative index")
    testif(len(v1) == 6, "len")

    v1[4] = -1    
    testif(v1[4] == -1, "setitem")
    v1[-3] = 10
    testif(v1[3] == 10, "setitem with negative index")
    
    try:
        x = v0[20]
    except IndexError:
        testif(True, "getitem with wrong index")
    else:  # no exception raised: fail!
        testif(False, "getitem with wrong index")

    try:
        v0[20] = 20
    except IndexError:
        testif(True, "setitem with wrong index")
    else:  # no exception raised: fail !
        testif(False, "setitem with wrong index")

    testif(str(v0) == "[0, 1, 2, 3, 4, 5]", "str")
    v2 = NVector([0,1,2,3,4,5])
    testif(v0 == v2, "eq")
    testif(v0 != v1, "ne")
    
    testif(NVector(1,2,3,4) + NVector(5,6,7,8) == NVector(6,8,10,12), "add NVector")
    testif(NVector(1,2,3,4) + 10 == NVector(11,12,13,14), "add number")
    testif(10 + NVector(1,2,3,4) == NVector(11,12,13,14), "radd number")

    testif(NVector(1,2,3,4) * NVector(3,-2,1,-1) == 3-4+3-4, "mul NVector")
    testif(NVector(1,2,3,4) * 2 == (1 + 2 + 3 + 4) * 2, "mul number")
    testif(2 * NVector(1,2,3,4) == (1 + 2 + 3 + 4) * 2, "mul number")

    testif(NVector.zeros(3) == NVector(0, 0, 0), "zeros 3")


if __name__ == "__main__":
    main()
    
