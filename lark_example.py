from lark import Lark, Transformer, v_args

# Example based off https://lark-parser.readthedocs.io/en/latest/examples/calc.html#sphx-glr-examples-calc-py

# Explanation / Summary
# ?<word> indicates the start of a rule.
#
# phrase "... -> <function>" where <function> will execute an actual function in the transformer class.
# E.g. "NAME "=" sum    -> assign_var" will call the 'assign_var' function in the CalculateTree class with two parameters name and value
calc_grammar = """
    ?start: sum
          | NAME "=" sum    -> assign_var

    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> sub

    ?product: atom
        | product "*" atom  -> mul
        | product "/" atom  -> div

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | NAME             -> var
         | "(" sum ")"

    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import sub, mul, truediv as div, neg
    # The "number" reduction will call the number function which just = float.
    number = float

    def add(self, a, b):
        # a,b will be floats based on the "number" reduction
        return a + b

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)


calc_parser = Lark(calc_grammar, parser='lalr', transformer=CalculateTree())
calc = calc_parser.parse


def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))


def test():
    print(calc("a = 1+2"))
    print(calc("1+a*-3"))


if __name__ == '__main__':
    test()
    # main()