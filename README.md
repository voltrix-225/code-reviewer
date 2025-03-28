
# Code Review Analyzer (CODE-REVIEWER)

## Overview
Code Review Analyzer (CODE-REVIEWER) is a command-line tool designed to analyze Python code for **syntax errors, code style violations, security risks, and complexity issues**. It combines multiple analyzers into one package to help developers improve their code quality efficiently.

CODE-REVIEWER supports running via the command line, allowing users to check their code by simply executing:
```sh
analyze <filename>
```
This project was built as part of a **FOSSHack hackathon**, ensuring it remains open-source and does not rely on external APIs.

## Features
- **Syntax Error Detection:** Identifies syntax errors in Python code.
- **Code Style Analysis:** Checks adherence to PEP 8 and other best practices using **Pylint**.
- **Security Checks:** Detects security vulnerabilities like:
  - Hardcoded API keys or passwords
  - Use of insecure functions like `eval()`
  - Unsafe subprocess execution
- **Code Complexity Analysis:** Evaluates:
  - **Cyclomatic Complexity** (number of independent execution paths)
  - **Nested Loops Depth**
  - **Recursive Function Calls**
- **Pylint Score Calculation:** Provides an overall code quality score.
- **Command-Line Usability:** Can be installed as a global package and used from any directory.

## Project Structure
```
code-reviewer/
├── src/
│   ├── analyzers/
│   │   ├── complexity_checker.py
│   │   ├── security_checker.py
│   │   ├── style_checker.py
│   │   ├── syntax_checker.py
│   │   ├── score.py
│   ├── main.py
├── tests/
│   ├── test_files/
│   ├── test_complexity.py
│   ├── test_security.py
├── setup.py
├── README.md
```

## Installation
To install CODE-REVIEWER as a package:
```sh
git clone <repo-url>
cd code-reviewer
pip install -e .
```

## Usage
To analyze a Python file:
```sh
analyze <filename>
```
Example:
```sh
analyze demo.py
```
Output Example:
```
Processing file: demo.py

CHECKING CODE SECURITY
- Security Risk: eval() found on line 10
- Hardcoded API key found

CHECKING CODE DESIGN
- PEP8 Violation: Function name should be snake_case

RUNNING COMPLEXITY ANALYSIS
- Cyclomatic Complexity: 5
- Found a Recursive Function 'fib' with 3 calls
- Total Complexity Score: 8

PYLINT SCORE: 7.5/10
```

## How It Works
### 1. **Syntax Checker**
- Uses Python’s built-in AST module to detect syntax errors.

### 2. **Code Style Checker**
- Uses Pylint to check for PEP 8 violations.
- Reports unused imports, naming issues, redundant conditions, etc.

### 3. **Security Checker**
- Scans for unsafe functions like `eval()`.
- Detects hardcoded API keys, passwords, and insecure subprocess calls.

### 4. **Complexity Analyzer**
- Uses **AST parsing** to calculate:
  - Cyclomatic complexity
  - Nested loop depth
  - Recursive function depth

### 5. **Pylint Score Calculator**
- Runs Pylint and extracts the final score, filtering out warnings and errors.

## Running Tests
To test the functionality:
```sh
pytest tests/
```

## Packaging & Distribution
To make CODE-REVIEWER globally accessible:
```sh
pip install -e .
```
This allows running `analyze <filename>` from any directory.

## Troubleshooting
### "analyze" is not recognized as a command
- Ensure the `Scripts` folder is in your system PATH:
  ```sh
  setx PATH "%PATH%;C:\Users\YourUser\AppData\Local\Programs\Python\Python39\Scripts"
  ```
- Restart the terminal and try again.


## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License
This project is open-source and licensed under the MIT License.

