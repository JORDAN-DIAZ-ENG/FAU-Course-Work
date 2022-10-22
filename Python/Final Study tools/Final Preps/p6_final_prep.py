def compose(f, g):
    """Returns a new function that is f(g(x)), i.e. (f o g)(x)
    f and g must be functions."""
    def compose_fun(x):    # inner function is visible only in compose()
        return f(g(x))     # However, we can call it if we have its obj. ref.
    return compose_fun
def upper_bound(maxval):
    return lambda x: min(x, maxval)
def square(x):
    return x * x
numb_lst = [4, -2, 0, 5, 3, -6, 3, 1, 5]
# computes list with squares of numbers from list or 20 if the square > 20:
limited_squares = map(compose(upper_bound(20), square), numb_lst)
print([x for x in limited_squares])