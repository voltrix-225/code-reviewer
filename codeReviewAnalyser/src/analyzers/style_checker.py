#checks style

import ast
import re

class CodeStyleChecker(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_FunctionDef(self, node):
        if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
            self.issues.append(f"Function name {node.name} should be in 'snake_case'")

        if not ast.get_docstring:
            self.issues.append(f"No Docstrings found for Function : {node.name}")

        if len(node.args.args) > 8:
            self.issues.append(f"Function : {node.name} has too many arguments")

        self.generic_visit(node)

    def visit_ClassDef(self, node):
        if not re.match(r'[A-Z][a-zA-Z0-9]*$', node.name):
            self.issues.append(f"Class Name : {node.name} should be in PascalCase")

        if not ast.get_docstring:
            self.issues.append(f"No Docstrings found for Function : {node.name}")

        self.generic_visit(node)

    def visit_Global(self, node):
        self.issues.append(f"Don't use 'Global Variables' : {','.join(node.names)}")
        
        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name) and not node.targets[0].id.startswith("_"):
            self.issues.append(f"Variable '{node.targets[0].id}' may be unused")
        
        self.generic_visit(node)

    def report_style_issues(self):
        if not self.issues:
            print("Found no code style issues")

        else:
            print(f"Found {len(self.issues) + 1} styling issues :")
            for issue  in self.issues:
                print(f"{issue}")


def check_code_style_issues(fp):
    with open(fp, "r", encoding = 'utf-8') as file:
        tree = ast.parse(file.read())
        check_code = CodeStyleChecker()
        check_code.visit(tree)
        check_code.report_style_issues()
        

