import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def fire_check(lst):
    tmp_board = deepcopy(board)
    for x, y in lst:
        tmp_board[x][y] = 1
    q = deque(fire)
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and tmp_board[nx][ny] == 0:
                tmp_board[nx][ny] = 2
                q.append((nx, ny))
    
    cnt = 0
    for x in range(N):
        for y in range(M):
            if tmp_board[x][y] == 0:
                cnt += 1
    return cnt

def dfs(lst, idx):
    global ans
    if len(lst) == 3:
        ans = max(ans, fire_check(lst))
        return
    
    for i in range(idx, len(empty)):
        lst.append(empty[i])
        dfs(lst, i + 1)
        lst.pop()

N, M = map(int, input().split())
board = []
fire = []
empty = []
ans = 0

for x in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for y in range(M):
        if tmp[y] == 2:
            fire.append((x, y))
        elif tmp[y] == 0:
            empty.append((x, y))

dfs([], 0)
print(ans)
