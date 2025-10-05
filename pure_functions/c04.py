# Case 1, impure
from copy import deepcopy

a = 1
b = 5


def foo_impure():
    global a
    a += 1
    return a*b


print(foo_impure())


# Case 1, pure
def foo_pure(a, b):
    a += 1
    return a*b, a


# We unpack the tuple on one line, then evaluate the expression as before in terms of a new variable
result, a = foo_pure(a, b)
print(result)


# Case 2, impure
lst = []


def bar_impure(lst):
    # Even though the function only reads its arguments and doesn't use the `global` keyword, it introduces side effects
    # through a mutable parameter
    lst.append(4)


bar_impure(lst)
print(lst)


# Case 2, pure
def bar_impure(lst):
    # Use a deepcopy to make any changes locally
    lst_local = deepcopy(lst)
    lst_local.append(4)
    # Return the changes
    return lst_local


lst = bar_impure(lst)
print(lst)


# Case 3, impure
c = 0


# This function doesn't seem to modify or read any kind of state, so the side effects aren't obvious...
def baz_impure():
    return quux_impure() ** 2


# ... but they are (in this case, not-very-well-)hidden in another function
def quux_impure():
    global c
    c += 2
    return c + 1


baz_impure()
print(c)


# Case 3, pure
def baz_pure(c):
    # The changes to `c` are received from `quux_pure` and passed up the chain to the global scope, where they can be
    # applied
    result, c = quux_pure(c)
    return result ** 2, c


def quux_pure(c):
    c += 2
    return c + 1, c


_, c = baz_pure(c)
print(c)
