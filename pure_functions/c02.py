import random

def next_number(memo=[0]):
    memo[0] += 1
    return memo[0]

# An unintuitive property
print(next_number() == next_number())

x = 4
z = 2

def impure_function_1(y, lst):
    global x
    # Printing or writing to a file is a side effect
    print(y)

    # Modifying state outside the function - whether that's a global variable, a mutable object passed in to the
    # function, or setting an attribute of `self` in a class function - is a side effect
    x += 1
    lst.append(y)

    # Awaiting user input is a side effect
    input("Press enter to continue")

    # Reading from global state or anything else not specified as an input to the function is not an "effect" but still
    # makes the function impure
    print(z)

    # Randomisation is in practice a side effect, as it changes the state of the hidden pseudorandom number generator.
    # Even if we found another way to randomise, it would still make the function impure, as true mathematical functions
    # are deterministic.
    print(random.randint(1, 4))

    # We've done so much stuff already, there's no need to return anything. But a pure function must return something in
    # order to be useful, because it can't have an effect in any other way.
    return

foo = 1
bar = 2

# This function is impure because it reads from and modifies the global state...
def impure_function_2():
    global foo
    foo = foo * bar

# ... but we can make it pure by making all the inputs and outputs explicit
def pure_function_2(foo, bar):
    # Since we didn't write `global foo`, the assignment here creates a local variable, so doesn't modify global state
    foo = foo * bar

    # We return the new values of the global variables we want to modify
    return foo

# Now
impure_function_2()
# does the same thing as
foo = pure_function_2(foo, bar)
# but the latter is purer and more explicit

# Some impure functions have return values as well as side effects...
def impure_function_3():
    global bar
    bar += 4

    return foo + bar

# ... so we can make them pure by returning a tuple containing the original return value and the modified state
def pure_function_3(foo, bar):
    bar += 4

    return foo + bar, bar

# So
print(impure_function_3())
# does the same thing as
result, bar = pure_function_3(foo, bar)
print(result)
