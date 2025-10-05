from fp_utils import *

second_of_four = lambda a: (lambda b: (lambda c: (lambda d: b)))

# Again, use `nfold_compose` to avoid writing things out many times
eighth_of_sixteen = ...  # This function should take 16 arguments one at a time, and then return the eighth one

apply = lambda f, x: f(x)

foo = lambda f, x: lambda y: f(x, y)


# You are welcome to write your own driver code to test, but remove all `lambda`s and `def`s from the driver code
# before submitting.
