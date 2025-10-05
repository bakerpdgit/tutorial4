from fp_utils import *

print(idem("Hello, world!"))
print(const("Two households")("both alike"))
print(succ(41))

# idem and const accept any type, including other functions
print(idem(42))
print(idem(const)("in dignity")("In fair Verona"))

# const takes arguments one at a time, so const(x) is a function of one argument which always returns x
print(idem(idem(const("where we lay")))("our scene"))

# const(const) always returns the function const, which itself expects two more arguments
print(const(const)("From ancient grudge")("break to new mutiny")("Where civil blood"))
