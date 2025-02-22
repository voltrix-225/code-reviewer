#checks pylint score

import subprocess
import re

def check_score(fp):
    score = subprocess.run(["pylint", fp], capture_output=True, text = True)
    match = re.search(r"Your code has been rated at ([\d\.]+)/10", score.stdout)
    return float(match.group(1)) 

