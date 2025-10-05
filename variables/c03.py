from fp_let import let, init_lets
LETS_ENABLED = init_lets()


def foo():
    print(locals())
    with let(x=6, y=7):
        print(locals())
        print(locals()["x"])
        print(f"{x} times {y} equals {x * y}")
    print(locals())


def bar():
    with let(string="Hello"):
        with let(string=string + ", world!"):
            with let(string=string.upper()):
                return string


if LETS_ENABLED:
    with let(a=4):
        print(a)

    foo()
    print(bar())
