import math

from fp_utils import *
from fp_let import let, init_lets
LETS_ENABLED = init_lets()


def tail(lst):
    match lst:
        case nil.nil:
            return lst
        case Cons(x, xs):
            return xs


@curry
def drop(n, lst):
    if n <= 0:
        return lst
    else:
        match lst:
            case nil.nil:
                return lst
            case Cons(x, xs):
                return drop(n - 1)(xs)


def foo(a, b, c):
    with let(a=a+b*c):
        with let(b=a*c, c=a**b):
            return a, b, c


def pythag(x, y):
    with let(squared_distance=x**2 + y**2):
        return math.sqrt(squared_distance)


def assemble_report(name, english_grade, history_grade, physics_exam_grade, physics_practical_grade):
    with let(result=name + " got " + str(english_grade) + "% in English, ",
             physics_total_grade=int(physics_exam_grade * 0.8 + physics_practical_grade * 0.2)):
        with let(result=result + str(history_grade) + "% in history, "):
            with let(result=result + "and " + str(physics_total_grade) + "% in physics"):
                return result, physics_total_grade


def two_to_the(n):
    return 2 ** n


def repeat_first_element(lst):
    match lst:
        case nil.nil:
            return nil
        case Cons(x, xs):
            return x ** x ** xs


if LETS_ENABLED:
    a = 3
    b = 2
    c = 4

    b = two_to_the(b)
    a, b, c = foo(a, b, c)
    c = pythag(a, b)
    report, physics_total_grade = assemble_report("The student", a * 5, b, c, 60)
    print(report)
    print(physics_total_grade)

    lst = 1 ** 2 ** 3 ** 5 ** 8 ** nil
    for _ in range(5):
        lst = repeat_first_element(lst)
    lst = drop(2)(lst)
    print(lst)
