I built a Simple Expression-to-JavaScript Transpiler that converts a small custom language (with statements like LET x = 10 + 20 and PRINT x * 2) into valid JavaScript code. The project helped me understand how real compilers work internally.

🔹 What the Transpiler Does

Reads custom language syntax (LET, PRINT, math expressions)

Converts the code into tokens

Parses the tokens using grammar rules

Creates an AST (Abstract Syntax Tree)

Translates the AST into equivalent JavaScript

Outputs clean, executable JavaScript

Example:

Input (my language):

LET x = 10 + 20
PRINT x * 2


Generated JavaScript:

let x = (10 + 20);
console.log(x * 2);


How I Built It (Your Technical Process)
1. Lexer (Tokenization)

I wrote a lexer that scans the input code and breaks it into tokens such as:

NUMBER

ID

LET

PRINT

PLUS / MINUS / MUL / DIV

Parentheses

This step taught me how programming languages convert raw text into meaningful symbols.

2. Parser + AST Generation

I used recursive-descent parsing to handle:

Expressions

Variables

Operator precedence

Assignments

I created AST nodes like:

NumberNode

VarNode

BinOpNode

LetNode

PrintNode

This helped me understand how languages structure code internally.

3. Transpiler (Code Generator)

After building the AST, I wrote a transpiler that:

Walks through the AST

Converts each node to JavaScript

Adds let declarations and console.log()

This step was very close to how Babel and TypeScript transpile code.

4. Putting It All Together

I connected the lexer → parser → transpiler through a main driver script.
The entire system works like a tiny compiler pipeline.
