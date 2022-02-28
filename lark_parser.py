from lark import Lark, Transformer, Token, v_args

speech_grammar: str = None

with open('grammar.lark', 'r') as f:
    speech_grammar = f.read()

@v_args(inline=True)    # Affects the signatures of the methods
class SpeechTree(Transformer):
    number = float


    # Default tokens should return strings
    def __default__(self, data, children, meta):
        if children:
            return " ".join(map(lambda t: str(t), children))
        else:
            return str(data)
    
    def start(self, predicates, statements):
        return f"""if ({predicates}) {{
            {statements}
        }}
        """
    
    def predicates(self, predicate):
        return str(predicate)
    
    def predicate_and(self, predicate, predicates):
        return f"{predicate} && {predicates}"
    
    def predicate_or(self, predicate, predicates):
        return f"{predicate} || {predicates}"

    def EQUALS(self, token):
        return "=="
    
    def NOT_EQUAL(self, token):
        return "!="

    def GREATER(self, token):
        return ">"
    
    def GREATER_OR_EQUAL(self, token):
        return ">="
    
    def LESS(self, token):
        return "<"

    def LESS_OR_EQUAL(self, token):
        return "<="

    def PLUS(self, token):
        return "+"
    
    def MINUS(self, token):
        return "-"

    def MULTIPLY(self, token):
        return "*"

    def DIVIDE(self, token):
        return "/"
    
    def MODULO(self, token):
        return "%"
    
    def NEGATION(self, token):
        return "!"

    def join_statements(self, stmt, stmts):
        return f"{stmt}\n{stmts}"

    def statement(self, stmt):
        return f"{stmt};"
    
    def declaration(self, name, type):
        return f"{type} {name}"
    
    def assignment(self, var, value):
        return f"{var} = {value}"

speech_parser = Lark(speech_grammar, parser='lalr', transformer=SpeechTree(visit_tokens=True))
parse_speech = speech_parser.parse


def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(parse_speech(s))


def test():
    print(calc("a = 1+2"))
    # print(calc("1+a*-3"))


if __name__ == '__main__':
    # test()
    main()