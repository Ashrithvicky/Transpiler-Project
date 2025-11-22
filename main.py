# main.py

from lexer import tokenize
from parser import Parser
from transpiler import Transpiler

def run(code):
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    transpiler = Transpiler()
    js_code = transpiler.transpile(ast)
    return js_code

if __name__ == "__main__":
    code = """LET x = 'ashrith' PRINT VIGNESHWAR"""
    output = run(code)
    print("Generated JavaScript:\n")
    print(output)
