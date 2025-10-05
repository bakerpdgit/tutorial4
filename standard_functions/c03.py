from fp_utils import *

plus_four = lambda x: x + 4

second_of_two = lambda x: (lambda y: y)

# Instead of writing anything out 30 times, use a standard function that takes a number as an argument
plus_thirty = lambda x: x + 30


print(plus_four(12))
print(second_of_two(1)(3))
print(plus_thirty(90))
