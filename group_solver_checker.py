from boj_crawler import get_problems_by_tag, sort_problems_by_level

def get_solved_user(solved_problem_list: list[dict], problem: int) -> list:
    solved_handles = []
    for solved_info in solved_problem_list:
        if problem in solved_info["problems"]:
            solved_handles.append(solved_info["handle"])

    return solved_handles

def get_unsolved_problems_by_tag(solved_problem_list: list[dict], tag: int) -> list[dict] | dict:
    res = get_problems_by_tag(tag)
    if not res["success"]:
        return res

    sort_res = sort_problems_by_level(res["problems"])
    if not sort_res["success"]:
        return sort_res

    problems = sort_res["problems"]

    result = []
    for problem in problems:
        solved_handle = get_solved_user(solved_problem_list, problem["id"])

        if len(solved_handle) == 0:
            result.append({"level": problem["level"], "URL": f"https://www.acmicpc.net/problem/{problem['id']}"})

    return result
