import requests, json
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2719.1708 Safari/537.36"}
TIER_LIST = ['Unrated/NotRatable', 'Bronze V', 'Bronze VI', 'Bronze III', 'Bronze II', 'Bronze I', 'Silver V', 'Silver VI', 'Silver III', 'Silver II', 'Silver I', 'Gold V', 'Gold VI', 'Gold III', 'Gold II', 'Gold I', 'Platinum V', 'Platinum VI', 'Platinum III', 'Platinum II', 'Platinum I', 'Diamond V', 'Diamond VI', 'Diamond III', 'Diamond II', 'Diamond I', 'Ruby V', 'Ruby VI', 'Ruby III', 'Ruby II', 'Ruby I']

def get_solved_problem(user):
    url = f'https://www.acmicpc.net/user/{user}'
    
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
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

def get_problems_by_tag(tag: int):
    url = f'https://www.acmicpc.net/problemset?sort=ac_desc&algo={tag}'

    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        problem_list = soup.select('#problemset > tbody > tr')

        tag_problems = [int(problem.select_one('.list_problem_id').get_text()) for problem in problem_list]

        return {"success": True, "problems": tag_problems}
    else:
        return {"success": False, "statusCode": response.status_code}

def sort_problems_by_level(problems: list[int]):
    url = f"https://solved.ac/api/v3/problem/lookup?problemIds={','.join(list(map(str, problems)))}"
    res = requests.get(url)

    if res.status_code == 200:
        problems = [{ 'id':  prob['problemId'], 'level': prob['level'], 'url': f"boj.kr/{prob['problemId']}"} for prob in res.json()]
        problems.sort(key=lambda x: x['level'])
        for prob in problems:
            prob['level'] = TIER_LIST[prob['level']]

        return {"success": True, "problems": problems}

    else:
        return {"success": False, "statusCode": res.status_code}

if __name__ == '__main__':
    print(get_solved_problem('jin99'))
    print(get_problems_by_tag('80'))
