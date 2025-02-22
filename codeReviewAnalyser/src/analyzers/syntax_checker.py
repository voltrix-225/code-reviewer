#checks syn

from pylint.lint import Run
import ast



def check_syntax_errors(fp):
    """
    Checks for syntax errors in a Python file using AST parsing.
    Returns True if syntax is correct, otherwise prints the error.
    """
     
    try:
        with open(fp, 'r', encoding='utf-8') as file:
            source_code = file.read()
        ast.parse(source_code)
        print(f"The syntax of {fp} is correct")
        return True
    except SyntaxError as e:
        print(f"Syntax error in {fp} at line {e.lineno} is {e.msg}")
        return False
