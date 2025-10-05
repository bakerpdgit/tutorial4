from fp_utils import *


def f(x):
    return x * 2


def g(x):
    return x ** 2


print((f |compose| g)(3))
print(nfold_compose(f)(5)(7))
print((idem |compose| f)(11))
print((f |compose| g |compose| f)(13))
