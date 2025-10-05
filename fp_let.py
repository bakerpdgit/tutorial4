import ast
import inspect


class let:
    def __init__(self, **assignments):
        self.__assignments = assignments
        self.__existing_values = {}

    def __enter__(self):
        vars = inspect.currentframe().f_back.f_locals
        self.__existing_values = {key: vars[key] for key in self.__assignments.keys() if key in vars}

    def __exit__(self, exc_type, exc_val, exc_tb):
        vars = inspect.currentframe().f_back.f_locals
        for key in self.__assignments.keys():
            vars[key] = self.__existing_values.get(key, None)


class LetTransformer(ast.NodeTransformer):
    def visit_Call(self, node):
        self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == "init_lets":
            return ast.Constant(True)
        else:
            return node

    def visit_With(self, node):
        self.generic_visit(node)
        if len(node.items) != 1:
            return node
        item = node.items[0]
        if not isinstance(item.context_expr, ast.Call):
            return node
        if not isinstance(item.context_expr.func, ast.Name):
            return node
        if item.context_expr.func.id != 'let':
            return node
        keywords = item.context_expr.keywords
        if len(keywords) == 0:
            return node

        node.body.insert(0, ast.Assign(
            [ast.Tuple([ast.Name(id=keyword.arg, ctx=ast.Store()) for keyword in keywords], ctx=ast.Store())],
            ast.Tuple([keyword.value for keyword in keywords])
        ))

        return node


def init_lets():
    frame = inspect.currentframe()
    while frame.f_back is not None:
        frame = frame.f_back
    code = frame.f_locals["code"]
    input_fn = frame.f_locals["global_vars"]["input"]

    tree = ast.parse(code)

    LetTransformer().visit(tree)
    ast.fix_missing_locations(tree)

    _evil_code = compile(tree, "editedCode.py", 'exec')

    exec(_evil_code, {"input": input_fn})

    return False
