from src.analyzers.complexity_checker import calculateCyclomaticComplexity, countNestedLoops, recursionCounter
from src.analyzers.style_checker import check_code_style_issues
from src.analyzers.security_checker import analyze_security, Pwd_checker, check_subprocess
from src.analyzers.syntax_checker import check_syntax_errors
from src.analyzers.score import check_score
import sys
import os


def analyze_file(fp):
    
    syntax = check_syntax_errors(fp)
    if not syntax:
        exit()

    print("\nCHECKING CODE SECURITY")
    code_security = analyze_security(fp)
    secrets = Pwd_checker(fp)
    subprocess = check_subprocess(fp)
    if not any ([code_security, secrets, subprocess]):
        print("No other security issues found.")

    print("\nCHECKING CODE DESIGN")
    check_code_style_issues(fp)
    print("\n")


    print("RUNNING COMPLEXITY ANALYSIS")
    cyclomatic_complexity = calculateCyclomaticComplexity(fp)
    nested_loop = countNestedLoops(fp)
    rec_name, rec_calls = recursionCounter(fp)
    if rec_name:
        print(f"Found a Recursive Function '{rec_name}', with {rec_calls} calls\n")
    print(f"The total complexity score is : {cyclomatic_complexity + nested_loop + rec_calls}\n")

    score = check_score(fp)
    print(f"THE PYLINT CODE SCORE IS : {score}/10")

def main():
    if len(sys.argv) < 2 :
        print("Usage : python scrript.py <filename>")
        sys.exit(1)

        
    fp = os.path.abspath(sys.argv[1])

    if not os.path.exists(fp):
        print("No such path exists")

    print(f"Processing file: {fp}\n")
    analyze_file(fp)

if __name__ == "__main__":
    main()