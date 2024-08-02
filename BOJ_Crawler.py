import requests, json
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2719.1708 Safari/537.36"}

def get_solved_problem(user):
    url = f'https://www.acmicpc.net/user/{user}'
    
    response = requests.get(url, headers=HEADERS)
    if (response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        problem_list = soup.select('body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div.panel-body > div > a')
    
        solved_problem = [int(problem.get_text()) for problem in problem_list]
        user_info = {
            "handle": user,
            "solved": len(solved_problem),
            "problems": solved_problem
        }

        curr_time = datetime.now()
        file_name = f'SolvedProblem_{user}_{curr_time.month}-{curr_time.day}-{curr_time.hour}-{curr_time.minute}.json'
        with open(file_name, 'w') as f:
            json.dump(user_info, f)

        return {"success": True, "fileName": file_name}
    else:
        return {"success": False, "statusCode": response.status_code}

def get_tag_problems(tag: int):
    url = f'https://www.acmicpc.net/problemset?sort=ac_desc&algo={tag}'

    response = requests.get(url, headers=HEADERS)
    if (response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        problem_list = soup.select('#problemset > tbody > tr')

        tag_problems = [int(problem.select_one('.list_problem_id').get_text()) for problem in problem_list]

        return {"success": True, "problems": tag_problems}
    else:
        return {"success": False, "statusCode": response.status_code}

if (__name__ == '__main__'):
    print(get_solved_problem('jin99'))
    print(get_tag_problems('80'))