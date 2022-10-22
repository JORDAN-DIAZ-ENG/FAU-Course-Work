students = [("Joe", 80), ("Alice", 70), ("Ana", 90)]

# part a
def students_average(stlst:list, sumgr:float, n:int):
    """Computes and returns the average GPA across all students in the list"""

    def calculate_sum_recursively(stlst, sumgr, n):
        if n == len(stlst) - 1:
            return stlst[0][1]

        return (stlst[0][1] + calculate_sum_recursively(stlst, sumgr + stlst[n + 1][1], n + 1))

    return calculate_sum_recursively(stlst, sumgr, n) / len(stlst)


avgr = students_average(students, 0.0, 0)
print(avgr)

