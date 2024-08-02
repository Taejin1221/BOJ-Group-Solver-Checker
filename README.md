# GroupSolverChecker
- BOJ 그룹의 멤버들이 공통으로 안 푼 문제를 출력해주는 스크립트
## How to Use
### 1. 멤버들의 푼 문제 확인
#### 1-1. 멤버들이 푼 문제 직접 전달
1. 그룹 멤버들이 푼 문제를 `.json` 파일에 `handle`, `problems`를 key로 하여 저장
    ```json
    [
        {
        "handle": "<handle>",
        "problems": [<problem>, <problem>, ...]
        }, {
        "handle": "<handle>",
        "problems": [<problem>, <problem>, ...]
        }, ...
    ]
    ```
2. `-s` 옵션으로 `.json` 파일을 명령행 인자로 넣어주어 실행
    ```
    python3 GroupSolverChecker -s <solved problem list>.json
    ```

#### 1-2. 멤버들의 BOJ Handle만 전달
1. 그룹 멤버들의 BOJ 핸들을 `.json` 파일에 `handles`를 key로하여 저장
    ```json
    { "handles": ["<handle>", "<handle>"] }
    ```
2. `-h` 옵션으로 `.json` 파일을 명령행 인자로 넣어주어 실행
    ```
    python3 GroupSolverChecker -h <group member list>.json
    ```

### 2. 멤버들이 안 푼 문제 확인
#### 2-1. 직접 확인할 문제 번호 입력
1. `Do you input manually or choose tag([m/t])?` 문구에서 `m` 입력
2. 문제 번호 입력
    1. 푼 멤버가 있을 때 `Handle: <handle>, <handle>` 형식으로 멤버 출력
    2. 푼 멤버가 없을 때 `No, https://boj.kr/<problem>` 형식으로 링크 출력

#### 2-2. 알고리즘 태그 입력
1. `Do you input manually or choose tag([m/t])?` 문구에서 `t` 입력
2. 알고리즘 태그 `숫자`로 입력
    - 태그 번호 확인 법
        1. [백준 알고리즘](https://www.acmicpc.net/problem/tags)에서 원하는 알고리즘 클릭
        2. `https://www.acmicpc.net/problemset?sort=ac_desc&algo=<tag>` 와 같은 형식에서 `<tag>`가 알고리즘의 태그 번호
3. 모든 그룹원들이 풀지 않은 문제가 `Unsolved: <problem>, 'https://boj.kr/<problem>'` 형식으로 출력

# BOJ_Crawler
- BOJ 홈페이지 크롤러
## get_solved_problem
- BOJ handle을 인자로 넣어주면 푼 문제들을 `SolvedProblem_<handle>_<month>-<day>-<hour>-<minute>.json` 형태로 저장
- Argument
    - `user`: BOJ Handle
- Return
    - `Dictionary`
        - 성공시 `{"success": True, "fileName": <json filename>}`
        - 실패시 `{"success": False, "statusCode": <error status code>}`

## get_tag_problem
- BOJ 알고리즘 tag를 인자로 넣어주면 알고리즘에 해당하는 문제들 반환
- Argument
    - `tag`: 알고리즘 tag (int)
- Return
    - `Dictionary`
        - 성공시 `{"success": True, "problems": <problem list>}`
        - 실패시 `{"success": False, "statusCode": <error status code>}`