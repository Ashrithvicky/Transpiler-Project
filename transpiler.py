# transpiler.py

class Transpiler:
    def transpile(self, statements):
        js_code = ""
        for stmt in statements:
            js_code += self.visit(stmt) + "\n"
        return js_code

    def visit(self, node):
        method_name = "visit_" + node.__class__.__name__
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return node.value

    def visit_VarNode(self, node):
        return node.name

    def visit_BinOpNode(self, node):
        return f"({self.visit(node.left)} {self.op_to_js(node.op)} {self.visit(node.right)})"

    def op_to_js(self, op):
        return {
            "PLUS": "+",
            "MINUS": "-",
            "MUL": "*",
            "DIV": "/"
        }[op]

    def visit_LetNode(self, node):
        return f"let {node.name} = {self.visit(node.expr)};"

    def visit_PrintNode(self, node):
        return f"console.log({self.visit(node.expr)});"
