# GroupSolverChecker
- BOJ 그룹의 멤버들이 공통으로 안 푼 문제를 출력해주는 스크립트
## 목차
- [How to Use](#how-to-use)
    - [1. 멤버들의 푼 문제 확인](#1-멤버들의-푼-문제-확인)
        - [1-1. 멤버들의 푼 문제 직접 전달](#1-1-멤버들이-푼-문제-직접-전달)
        - [1-2. 멤버들의 BOJ Handle만 전달](#1-2-멤버들의-boj-handle만-전달)
    - [2. 멤버들이 안 푼 문제 확인](#2-멤버들이-안-푼-문제-확인)
        - [2-1. 직접 확인할 문제 번호 입력](#2-1-직접-확인할-문제-번호-입력)
        - [2-2. 알고리즘 태그 입력](#2-2-알고리즘-태그-입력)
- [모듈](#모듈)
    - [boj_crawler.py](#boj_crawlerpy)
        - [get_solved_by_handle](#get_solved_by_handle)
        - [get_solved_by_handle_bulk](#get_solved_by_handle_bulk)
        - [get_problems_by_tag](#get_problems_by_tag)
        - [sort_problems_by_level](#sort_problems_by_level)
    - [group_solver_checker.py](#group_solver_checkerpy)
        - [get_solved_user](#get_solved_user)
        - [get_unsolved_problems_by_tag](#get_unsolved_problems_by_tag)

## How to Use
### 1. 멤버들의 푼 문제 확인
#### 1-1. 멤버들이 푼 문제 직접 전달
1. 그룹 멤버들이 푼 문제를 `.json` 파일에 `handle`, `problems`를 key로 하여 저장
    ```json
    [
        {
        "handle": "<handle>",
        "problems": [1000, 1001, 1002]
        }, {
        "handle": "<handle>",
        "problems": [2000, 2001]
        }, 
    ]
    ```
2. `-s` 옵션으로 `.json` 파일을 명령행 인자로 넣어주어 실행
    ```
    python3 main.py -s <solved problem list>.json
    ```

#### 1-2. 멤버들의 BOJ Handle만 전달
1. 그룹 멤버들의 BOJ 핸들을 `.json` 파일에 `handles`를 key로하여 저장
    ```json
    { "handles": ["<handle>", "<handle>"] }
    ```
2. `-h` 옵션으로 `.json` 파일을 명령행 인자로 넣어주어 실행
    ```
    python3 main.py -h <group member list>.json
    ```

### 2. 멤버들이 안 푼 문제 확인
#### 2-1. 직접 확인할 문제 번호 입력
1. `태그를 선택하실 건가요? 수동으로 번호를 입력하실건가요? [t/m]` 문구에서 `m` 입력
2. 문제 번호 입력
    1. 푼 멤버가 있을 때 아래 형식으로 멤버 출력
        ```
        아래 사람이 문제를 풀었습니다.
        <handle1>, <handle2>
        ```
    2. 푼 멤버가 없을 때 `아무도 이 문제를 풀지 않았습니다. (https://www.acmicpc.net/problem/<problem>)` 형식으로 링크 출력

#### 2-2. 알고리즘 태그 입력
1. `태그를 선택하실 건가요? 수동으로 번호를 입력하실건가요? [t/m]` 문구에서 `t` 입력
2. 알고리즘 태그 `숫자`로 입력
    - 태그 번호 확인 법
        1. [백준 알고리즘](https://www.acmicpc.net/problem/tags)에서 원하는 알고리즘 클릭
        2. `https://www.acmicpc.net/problemset?sort=ac_desc&algo=<tag>` 와 같은 형식에서 `<tag>`가 알고리즘의 태그 번호
3. 모든 그룹원들이 풀지 않은 문제가 `Diff: <level>, URL: https://www.acmicpc.net/problem/<problem>` 형식으로 출력

# 모듈
## boj_crawler.py
- BOJ 홈페이지 크롤러
### get_solved_by_handle
- BOJ handle을 인자로 넣어주면 푼 문제들을 `SolvedProblem_<handle>_<month>-<day>-<hour>-<minute>.json` 형태로 저장
- Argument
    - `user`: BOJ Handle
- Return
    - `Dictionary`
        - 성공시 `{"success": True, "problems": <solved problem list>}`
        - 실패시 `{"success": False, "statusCode": <error status code>}`

### get_solved_by_handle_bulk
- BOJ handle 리스트를 넣어주면 푼 문제들을 `get_solved_by_handle`과 같은 형식으로 저장
- 이후 푼 문제 정보를 반환
- Argument
    - `user`: BOJ Handle
- Return
    - `List[Dictionary]`
        ```
        [
            {
                "handle": <handle>,
                "solved": <number of solved>,
                "problems": [<prob1>, <prob2>, ... ]
            }, {
                "handle": <handle>,
                "solved": <number of solved>,
                "problems": [<prob1>, <prob2>, ... ]
            }
        ]`
        ```
    - 만약 특정 handle의 정보를 얻지 못했다면 아래 오류와 함께 `solved`에 -1, `problems`에 아무것도 저장되지 않음
        `ERROR - Failed to get {user}'s problem list - Error code: {result['statusCode']}`
        

### get_problems_by_tag
- BOJ 알고리즘 tag를 인자로 넣어주면 알고리즘에 해당하는 문제들 반환
- Argument
    - `tag`: 알고리즘 tag (int)
- Return
    - `Dictionary`
        - 성공시 `{"success": True, "problems": <problem list>}`
        - 실패시 `{"success": False, "statusCode": <error status code>}`

### sort_problems_by_level
- 문제 리스트가 주어지면 난이도 별로 정렬
- Argument
    - `problems`: 문제 번호 리스트
- Return
    - `Dictionary`
        - 성공시 `{"success": True, "problems": [{"id": <problem id>, "level": <problem level>, "url": <problem url>}]}`
        - 실패시 `{"success": False, "statusCode": <error status code>}`

## group_solver_checker.py
### get_solved_user
- 사용자의 푼 문제 정보와 문제가 주어지면 해당 문제를 푼 유저를 반환
- Argument
    - `solved_problem_list`: 사용자의 푼 문제 정보
        - [get_solved_by_handle_bulk](###get_solved_by_handle_bulk)의 반환값과 동일한 형태 
    - `problem`: 문제 번호
- Return
    - `List`
        - `[<handle>, <handle>, ...]` 
       
### get_unsolved_problems_by_tag
- 사용자의 푼 문제 정보와 태그가 주어지면 해당 태그의 안푼 문제들을 난이도 순으로 정렬해서 반환
- Argument
    - `solved_problem_list`: 사용자의 푼 문제 정보
        - [get_solved_by_handle_bulk](###get_solved_by_handle_bulk)의 반환값과 동일한 형태 
    - `tag`: 태그 번호
- Return
    - `Dictionary`
        ```
        [
            {
                "level": <difficulty>,
                "URL": <url>
            }, {
                "level": <difficulty>,
                "URL": <url>
            }
        ]
        ```