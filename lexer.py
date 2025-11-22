# lexer.py

import re

TOKEN_SPEC = [
    ("NUMBER",   r'\d+'),
    ("LET",      r'LET'),
    ("PRINT",    r'PRINT'),
    ("ID",       r'[A-Za-z_][A-Za-z0-9_]*'),
    ("PLUS",     r'\+'),
    ("MINUS",    r'-'),
    ("MUL",      r'\*'),
    ("DIV",      r'/'),
    ("ASSIGN",   r'='),
    ("LPAREN",   r'\('),
    ("RPAREN",   r'\)'),
    ("SKIP",     r'[ \t]+'),
    ("NEWLINE",  r'\n'),
]


TOKEN_REGEX = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"

def tokenize(code):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, code):
        kind = match.lastgroup
        value = match.group()

        if kind == "SKIP":
            continue
        if kind == "NEWLINE":
            continue

        tokens.append(Token(kind, value))
    return tokens

