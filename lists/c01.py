from fp_utils import *

# A list, in the sense of functional programming
# Note the `FList` constructor in the representation - we are defining a new list type, not using the old one
print(1 ** 2 ** 3 ** nil)

# Alternative ways to write lists
print(Cons(1, Cons(2, Cons(3, nil))))  # Likely to be too cumbersome
print(flist([1, 2, 3]))                # Viable

# Familiar list operations like concatenation or element access don't exist yet. We will define them ourselves later.
try:
    print((1 ** nil) + (2 ** nil))
except TypeError as e:
    print(e)

try:
    print((1 ** nil)[0])
except TypeError as e:
    print(e)
