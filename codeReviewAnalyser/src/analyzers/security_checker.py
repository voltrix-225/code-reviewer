import ast

"""
HERE THE SECURITY ANALYSER CLASS IS PART OF AST, WHICH VISITS EACH NODE IN 
ABSTRACT SYNTAX TREE AND CHECKS FOR CERTAIN SECURITY RISKS IN CODE.
"""

#CHECKS FOR EVAL OR EXEC IN CODE
class Security_Analyser(ast.NodeVisitor):
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in ["eval", "exec"]:
            print(f"Security Warning: Use of {node.func.id} at line {node.lineno}")
        self.generic_visit(node)

def analyze_security(fp):
    with open(fp, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())
    detector = Security_Analyser()
    detector.visit(tree)

#CHECKS FOR PWDS OR API KEYS
class PwdDetector(ast.NodeVisitor):
    def visit_Assign(self, node):
        if isinstance(node.value, ast.Constant) and ('API' or 'Pwd' or 'password')in ast.dump(node.targets[0]):
            print(f"Warning: Potential secret exposure at line {node.lineno}")
        self.generic_visit(node)

def Pwd_checker(fp):
    with open(fp, "r", encoding= "utf-8") as file:
        tree = ast.parse(file.read())
    PwdDetector().visit(tree)

#CHECKS FOR subprocess.run()
class SubprocessAnalyser(ast.NodeVisitor):
    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and node.func.attr == "run":
            print(f"Security Warning : use of 'subprocess.run()' at line no. {node.lineno}")
        self.generic_visit(node)

def check_subprocess(fp):
    with open(fp, "r", encoding= "utf-8") as file:
        tree = ast.parse(file.read())
    SubprocessAnalyser().visit(tree)
