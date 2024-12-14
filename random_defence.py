import json
import sys

from solved_ac_api import get_random_defence, get_problem_info

with open(sys.argv[2], "rt") as f:
    handles = json.load(f)["handles"]

if sys.argv[1] == "-g":
    problems = get_random_defence(handles, "g")
else:
    problems = get_random_defence(handles, "s")

for problem in problems[:5]:
    problem_info = get_problem_info(problem)
    print(f"[BOJ {problem}: {problem_info['titleKo']}](https://www.acmicpc.net/problem/{problem})")
