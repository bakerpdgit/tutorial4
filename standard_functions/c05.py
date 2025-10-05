from functools import partial

from fp_utils import *

# Two possible definitions for the function `const`
const_curried = lambda x: (lambda y: x)
const_uncurried = lambda x, y: x

# Curried functions expect their parameters in a different order to uncurried functions
print(const_curried(3)(4))
print(const_uncurried(5, 6))

f = const_curried(const_curried)
g = partial(const_uncurried, const_uncurried)

# When functions can return other functions, they naturally expect their arguments to be passed one at a time. It's
# clearer, then, if every function expects its arguments one at a time
print(f(7)(8)(9))
print(g(10)(11, 12))  # Difficult to remember the diverse lengths of parameter lists


def plus(a, b):
    return a + b


# Convert a binary function to a curried function
print(curry(plus)(3)(4))


# Python's decorator syntax can be helpful with curry
@curry
def times(a, b):
    return a * b


print(times(5)(6))

# Convert a curried function to a binary function
print(uncurry(times)(7, 8))


# For technical reasons, curry and uncurry only work with binary functions. I've provided curry3, curry4, uncurry3,
# and uncurry4 in case they're helpful
@curry4
def minkowski(x, y, z, t):
    return t**2 - x**2 - y**2 - z**2


print(minkowski(10)(3)(4)(5))
