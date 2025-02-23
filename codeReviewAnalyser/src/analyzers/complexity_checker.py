#checks complexity


import ast

class CyclomaticComplexityChecker(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 0

    def visit_If(self, node):
        """Checks complexity arising from 'if' statements"""
        print(f"Encountered 'if' statement at line number {node.lineno}")
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        """Checks complexity arising from 'while' loops"""
        print(f"Encountered 'while' statement at line number {node.lineno}")
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        """Checks complexity arising from 'for' loops"""
        print(f"Encountered 'for' loop at line number {node.lineno}")
        self.complexity += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        """Checks complexity arising from 'boolean' operations"""
        print(f"Encountered Boolean Operation at line number {node.lineno}")
        self.complexity += 1
        self.generic_visit(node)
        
    def visit_Try(self, node):
        """Checks complexity arising from 'try' blocks"""
        print(f"Encountered 'Try Block' at line number {node.lineno}")
        self.complexity += 1
        self.generic_visit(node)


def calculateCyclomaticComplexity(fp):
    with open(fp, "r", encoding = "utf-8") as file:
        tree = ast.parse(file.read())
        cyclomatic_complexity = CyclomaticComplexityChecker() 
        cyclomatic_complexity.visit(tree)
        return cyclomatic_complexity.complexity 


class NestedLoopCounter(ast.NodeVisitor):
    def __init__(self):
        self.max_depth = 0
        self.current_depth = 0

    def visit_For(self, node):
        """Checks complexity arising from nested 'for' loops"""
        self.current_depth += 1
        self.max_depth = max(self.current_depth, self.max_depth)
        self.generic_visit(node)
        self.current_depth -= 1  #BACKTRACKS AFTER VISITING CHILD NODES


    def visit_While(self, node):
        """Checks complexity arising from nested 'while' loops"""
        self.current_depth += 1
        self.max_depth = max(self.current_depth, self.max_depth)
        self.generic_visit(node)
        self.current_depth -= 1
        

def countNestedLoops(fp):
    with open(fp, "r", encoding = "utf-8") as file:
        tree = ast.parse(file.read())
        nestedloop_complexity = NestedLoopCounter()
        nestedloop_complexity.visit(tree)
        return nestedloop_complexity.max_depth



class RecursiveComplexityCounter(ast.NodeVisitor):
    def __init__(self):
        self.recursive_functions = set()  #STORES THE FUNCTIONS THAT CALL THEMSELVES
        self.recfunc_dict = {'name': None, 'calls': 0}

    def visit_FunctionDef(self, node):
        function_name = node.name    #GET FUNCTION NAME
        
        for child in ast.walk(node):
            if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                if child.func.id == function_name:
                    self.recfunc_dict['name'] = function_name
                    self.recfunc_dict['calls'] += 1

        self.generic_visit(node)



def recursionCounter(fp):
       with open(fp, "r", encoding = "utf-8") as file:
        tree = ast.parse(file.read())
        recursive_complexity = RecursiveComplexityCounter()
        recursive_complexity.visit(tree)
        return recursive_complexity.recfunc_dict['name'], recursive_complexity.recfunc_dict['calls']  
 


