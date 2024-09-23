from copy import deepcopy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board, chess = [], []
for x in range(N) :
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for y in range(M) :
        if tmp[y] in [1, 2, 3, 4, 5] :
            chess.append((tmp[y], x, y))

def fill(board, direction, x, y) :
    for d in direction :
        nx, ny = x, y
        while True :
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6 :
                board[nx][ny] = -1
            else :
                break

def dfs(level, board) :
    global ans
    if level == len(chess) :
        cnt = 0
        for i in range(N) :
            cnt += board[i].count(0)
        ans = min(ans, cnt)
        return

    tmp = deepcopy(board)
    chess_num, x, y = chess[level]
    for direction in directions[chess_num] :
        fill(tmp, direction, x, y)
        dfs(level + 1, tmp)
        tmp = deepcopy(board)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
directions = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [0, 3]], [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], [[0, 1, 2, 3]]]
ans = 1e9
dfs(0, board)
print(ans)
