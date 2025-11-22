# parser.py

class NumberNode:
    def __init__(self, value):
        self.value = value

class VarNode:
    def __init__(self, name):
        self.name = name

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class LetNode:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class PrintNode:
    def __init__(self, expr):
        self.expr = expr

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, type_):
        token = self.current()
        if token and token.type == type_:
            self.pos += 1
            return token
        raise Exception(f"Expected {type_}, got {token}")

    def parse(self):
        statements = []
        while self.current():
            statements.append(self.statement())
        return statements

    def statement(self):
        token = self.current()

        if token.type == "LET":
            return self.let_statement()
        if token.type == "PRINT":
            return self.print_statement()

        raise Exception("Unknown statement!")

    def let_statement(self):
        self.eat("LET")
        var_name = self.eat("ID").value
        self.eat("ASSIGN")
        expr = self.expr()
        return LetNode(var_name, expr)

    def print_statement(self):
        self.eat("PRINT")
        expr = self.expr()
        return PrintNode(expr)

    def expr(self):
        node = self.term()

        while self.current() and self.current().type in ("PLUS", "MINUS"):
            op = self.eat(self.current().type)
            node = BinOpNode(node, op.type, self.term())

        return node

    def term(self):
        node = self.factor()

        while self.current() and self.current().type in ("MUL", "DIV"):
            op = self.eat(self.current().type)
            node = BinOpNode(node, op.type, self.factor())

        return node

    def factor(self):
        token = self.current()

        if token.type == "NUMBER":
            self.eat("NUMBER")
            return NumberNode(token.value)

        if token.type == "ID":
            self.eat("ID")
            return VarNode(token.value)

        if token.type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node

        raise Exception("Unexpected token in factor!")
