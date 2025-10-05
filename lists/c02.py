from fp_utils import *


def sum(lst):
    match lst:
        case Cons(x, xs):
            return x + sum(xs)
        case nil.nil:
            return 0


def concat(left, right):
    match left:
        case Cons(x, xs):
            return x ** concat(xs, right)
        case nil.nil:
            return right
