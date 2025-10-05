import dataclasses
import inspect
from abc import ABC, abstractmethod
from typing import TypeVar, Never


class infix:
    def __init__(self, func, *, is_unary=False):
        self.__func = func
        self.__is_unary = is_unary

    def __ror__(self, left_arg):
        return infix(lambda b, s=self, a=left_arg: s.__func(a, b), is_unary=True)

    def __or__(self, right_arg):
        if self.__is_unary:
            # Both arguments were passed using infix notation: a |f| b
            return self.__func(right_arg)
        else:
            # Slicing on the right: (f| b)(a)
            return lambda a, s=self, b=right_arg: s.__func(a, b)

    def __pow__(self, right_arg):
        return infix(lambda a, s=self, b=right_arg: s.__func(a, b), is_unary=True)

    def __rpow__(self, left_arg):
        if self.__is_unary:
            # Both arguments were passed using infix notation: a **f** b
            return self.__func(left_arg)
        else:
            # Slicing on the left: (a **f)(b)
            return lambda b, s=self, a=left_arg: s.__func(a, b)

    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)


class let:
    def __init__(self, **assignments):
        self.__assignments = assignments
        self.__existing_values = {}

    def __enter__(self):
        vars = inspect.currentframe().f_back.f_locals
        self.__existing_values = {key: vars[key] for key in self.__assignments.keys() if key in vars}

    def __exit__(self, exc_type, exc_val, exc_tb):
        vars = inspect.currentframe().f_back.f_locals
        for key in self.__assignments.keys():
            vars[key] = self.__existing_values.get(key, None)


# Standard functions
idem = lambda x: x
const = lambda x: (lambda y: x)

def undefined(x):
    return undefined(x)

succ = lambda n: n + 1
compose = infix(lambda f, g: lambda x: f(g(x)))

curry = lambda f: lambda x: lambda y: f(x, y)
uncurry = lambda f: lambda x, y: f(x)(y)
curry3 = lambda f: lambda x: lambda y: lambda z: f(x, y, z)
curry4 = lambda f: lambda x: lambda y: lambda z: lambda w: f(x, y, z, w)
uncurry3 = lambda f: lambda x, y, z: f(x)(y)(z)
uncurry4 = lambda f: lambda x, y, z, w: f(x)(y)(z)(w)

@curry
def nfold_compose(f, n):
    def f1(x):
        result = x
        for i in range(n):
            result = f(result)
        return result
    return f1


# Lists
def flist(lst):
    match lst:
        case []:
            return nil
        case [x, *xs]:
            return Cons(x, flist(xs))

A = TypeVar('A', covariant=True)

class FList[A](ABC):
    def __rpow__(self, x):
        return Cons(x, self)

    @abstractmethod
    def _to_py_list(self) -> list[A]:
        raise NotImplementedError

    def __str__(self):
        return "flist(" + str(self._to_py_list()) + ")"

@dataclasses.dataclass
class Cons[A](FList[A]):
    head: A
    tail: 'FList[A]'

    def _to_py_list(self) -> list[A]:
        return [self.head] + self.tail._to_py_list()

class Nil(FList[Never]):
    @property
    def nil(self): return self

    def _to_py_list(self) -> list[Never]:
        return []

nil = Nil()

def head(l):
    match l:
        case nil.nil: raise ValueError("Head of empty list")
        case Cons(x, _): return x

def tail(l):
    match l:
        case nil.nil:
            raise ValueError("Tail of empty list")
        case Cons(_, xs):
            return xs

@curry3
def fold(c, n, l):
    match l:
        case nil.nil: return n
        case Cons(x, xs): return c(x, fold(c)(n)(xs))

@curry
def map_list(f, l):
    match l:
        case nil.nil: return nil
        case Cons(x, xs): return f(x) ** map_list(f)(xs)

@curry
def filter_list(f, l):
    match l:
        case nil.nil: return nil
        case Cons(x, xs):
            if f(x):
                return x ** filter_list(f)(xs)
            else:
                return filter_list(f)(xs)


# Types
# to = infix(lambda t1, t2: Callable[t1, t2])


# Monads
bind = infix(lambda xm, f: xm.bind(f))

class Monad(ABC):
    @staticmethod
    def eta(val): raise NotImplementedError

    def bind(self, f): raise NotImplementedError

class State(Monad):
    def __init__(self, *, val, state):
        self.__val = val
        self.__state = state

    @staticmethod
    def eta(val):
        return State(val=val, state={})

    def bind(self, f):
        new = f(self.__val)
        return State(val=new.__val, state=self.__state | new.__state)

    @staticmethod
    def set(**kwargs):
        return State(val=None, state=kwargs)

class MaybeMonad(Monad):
    def __init__(self, *, is_present, val=None):
        self.__is_present = is_present
        self.__val = val

    @staticmethod
    def eta(val):
        return MaybeMonad(is_present=True, val=val)

    @staticmethod
    def failure():
        return MaybeMonad(is_present=False)

    def bind(self, f):
        return f(self.__val) if self.__is_present else self.failure()

class ListMonad(Monad):
    def __init__(self, *, options):
        self.__options = options

    @staticmethod
    def eta(val):
        return ListMonad(options=[val])

    def bind(self, f):
        return ListMonad(options=[option for monad in map(f, self.__options) for option in monad.__options])
