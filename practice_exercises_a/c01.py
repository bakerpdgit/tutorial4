import math

from fp_utils import *


def foo():
    global a, b, c
    a = a + b * c
    b, c = a * c, a ** b


def pythag():
    global c
    squared_distance = a**2 + b**2
    c = math.sqrt(squared_distance)


def assemble_report(name, english_grade, history_grade, physics_exam_grade, physics_practical_grade):
    global physics_total_grade
    physics_total_grade = int(physics_exam_grade * 0.8 + physics_practical_grade * 0.2)
    result = name + " got " + str(english_grade) + "% in English, "
    result = result + str(history_grade) + "% in history, "
    result = result + "and " + str(physics_total_grade) + "% in physics"
    return result


def two_to_the():
    global b
    b = 2 ** b


def repeat_first_element(lst):
    if lst != []:
        lst.insert(0, lst[0])


def tail(lst):
    if lst == []:
        pass
    else:
        del lst[0]


@curry
def drop(n, lst):
    if n <= 0:
        return
    elif lst == []:
        pass
    else:
        del lst[0]
        drop(n - 1)(lst)


a = 3
b = 2
c = 4
physics_total_grade = 0

two_to_the()
foo()
pythag()
print(assemble_report("The student", a * 5, b, c, 60))
print(physics_total_grade)

lst = [1, 2, 3, 5, 8]
for _ in range(5):
    repeat_first_element(lst)
drop(2)(lst)
print(lst)
