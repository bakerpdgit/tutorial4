def f(x):
    return x + 2


z = f(2)


def f(x):
    return x + 3


print(z == f(2))  # Previously, `z = f(2)`, but now, `z != f(2)`. This isn't possible in pure maths


y = 4
z = y
y = 5
print(z == y)  # Previously, `z = y`, but now, `z != y`. This isn't possible in pure maths
