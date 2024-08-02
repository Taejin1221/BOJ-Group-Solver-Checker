import json, sys

from BOJ_Crawler import get_solved_problem, get_tag_problems

if (sys.argv[1] == '-s' or sys.argv[1] == '--solved'): # Group member들이 푼 문제 list가 주어졌을 때
    with open(sys.argv[2]) as f:
        solved_problem_list = json.load(f)

elif (sys.argv[1] == '-h' or sys.argv[1] == '--handle'): # 푼 문제 list가 아닌 handle만 주어졌을 때
    with open(sys.argv[2]) as f:
        group_members_list = json.load(f)['handles']

    file_list = []
    for member in group_members_list:
        res = get_solved_problem(member)
        if (res['success']):
            file_list.append(res['fileName'])
            print(res['fileName'])
        else:
            print(f"Error: {member}, {res['statusCode']}")
            sys.exit(1)

    solved_problem_list = []
    for file in file_list:
        with open(file) as f:
            solved_problem_list.append(json.load(f))

else:
    print(f"usage: python3 {sys.argv[0]} [-s, -h] FILE\n")
    print("options:")
    print("  -s, --solved: Give solved problem list of all members.")
    print("  -h, --handle: Give all member's handles.")

    sys.exit(1)

oper = input('Do you input manually or choose tag([m/t])? ')
if (oper == 'm'):
    problem = input("Input problem [int/q]: ")
    while (problem != 'q'):
        try:
            problem = int(problem)

            solved_handle = []
            for solved_list in solved_problem_list:
                if (problem in solved_list['problems']):
                    solved_handle.append(solved_list['handle'])

            if (len(solved_handle) > 0):
                print(f"Handle: {', '.join(solved_handle)}")
            else:
                print(f"No, https://boj.kr/{problem}")
        except ValueError as e:
            print('Error: You can input only "int" and "q"')
        print('')

        problem = input("Input problem number: ")

    print("quit")
elif (oper == 't'):
    tag = input('Input tag: ')
    res = get_tag_problems(tag)
    if (res['success']):
        problems = res['problems']
    else:
        print(f"Error: {tag}, {res['statusCode']}")
        sys.exit(1)

    for problem in problems:
        solved_handle = []
        for solved_list in solved_problem_list:
            if (problem in solved_list['problems']):
                solved_handle.append(solved_list['handle'])

        if (len(solved_handle) == 0):
            print(f"Unsolved: {problem}, 'https://boj.kr/{problem}'")