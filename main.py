import json
import sys

from boj_crawler import get_solved_by_handle_bulk
from group_solver_checker import get_solved_user, get_unsolved_problems_by_tag

if sys.argv[1] == '-h' or sys.argv[1] == '--handle':
    with open(sys.argv[2], "rt") as f:
        handles = json.load(f)["handles"]
    solved_problem_list = get_solved_by_handle_bulk(handles)
elif sys.argv[1] == '-s' or sys.argv[1] == '--solved':
    with open(sys.argv[2], "rt") as f:
        solved_problem_list = json.load(f)
else:
    print("올바른 명령어를 입력하세요.")
    sys.exit(1)

oper = input("태그를 선택하실 건가요? 수동으로 번호를 입력하실건가요? [t/m] ")
if oper == "m":
    problem = input("문제 번호를 입력하세요 [int/q]: ")
    while problem != "q":
        problem = int(problem)
        solved_handles = get_solved_user(solved_problem_list, problem)
        if len(solved_handles):
            print("아래 사람이 문제를 풀었습니다.")
            print(", ".join(solved_handles), end="\n\n")
        else:
            print(f"아무도 이 문제를 풀지 않았습니다. (https://www.acmicpc.net/problem/{problem})", end="\n\n")

        problem = input("문제 번호를 입력하세요 [int/q]: ")
elif oper == "t":
    tag = input("태그 번호를 입력하세요 [int/q]: ")
    if tag == "q":
        sys.exit(0)

    tag = int(tag)
    unsolved_list = get_unsolved_problems_by_tag(solved_problem_list, tag)

    for unsolve in unsolved_list:
        print(f"Diff: {unsolve['level']}, URL: {unsolve['URL']}")
else:
    print("올바른 명령어를 입력하세요")
