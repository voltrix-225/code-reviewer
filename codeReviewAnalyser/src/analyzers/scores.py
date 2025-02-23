"""This module will calcutate PyLint scores for a program"""

import subprocess
import re

def check_score(fp):
    score = subprocess.run(["pylint", fp], capture_output=True, text = True) #runs pylint for file
    match = re.search(r"Your code has been rated at ([\d\.]+)/10", score.stdout)  #retreives a rating, which is formatted via regex
    return float(match.group(1)) 

