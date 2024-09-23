import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = []
hospital = []
cure_board = []
ans = []
for x in range(N) :
    tmp = list(map(int, input().split()))
    cure_board_tmp = []
    for y in range(N) :
        if tmp[y] == 2 :
            hospital.append((x, y))
            cure_board_tmp.append(-1)
        elif tmp[y] == 1 :
            cure_board_tmp.append(-2)
        else :
            cure_board_tmp.append(1e9)
    cure_board.append(cure_board_tmp)

def select_hospital(lst, level) :
    if len(lst) < M and level < len(hospital) :
        select_hospital(lst + [hospital[level]], level + 1)
        select_hospital(lst, level + 1)
    elif len(lst) == M :
        cure(lst)

def cure(lst) :
    tmp_ans = 0
    cboard = deepcopy(cure_board)
    for x, y in lst :
        cboard[x][y] = 0
    q = deque(lst)
    while q :
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N :
                if cboard[nx][ny] == -2 :
                    continue
                elif cboard[nx][ny] == -1 or cboard[x][y] + 1 < cboard[nx][ny] :
                    cboard[nx][ny] = cboard[x][y] + 1
                    q.append((nx, ny))
                    tmp_ans = max(tmp_ans, cboard[x][y] + 1)
    result = check(cboard)
    if result != -1 :
        ans.append(result)

def check(cboard) :
    tmp_ans = 0
    for x in range(N) :
        for y in range(N) :
            if cboard[x][y] == 1e9 :
                return -1
            elif (x, y) not in hospital :
                tmp_ans = max(tmp_ans, cboard[x][y])
    return tmp_ans
    
select_hospital([], 0)
if not ans :
    print(-1)
else :
    print(min(ans))
