import json

import requests


def get_random_defence(handles: list[str], tier: str = "g") -> list[int]:
    query = "-@" + "+-@".join(handles) + "+%ko"
    if tier == "g":
        query += "+*g"
    elif tier == "s":
        query += "+*s"
    else:
        raise ValueError("올바르지 않은 Tier 값입니다. [g or s]")

    response = requests.get(f"https://solved.ac/api/v3/search/problem?direction=asc&sort=random&query={query}")
    items = json.loads(response.text)["items"]

    problems = [item["problemId"] for item in items]

    return problems
