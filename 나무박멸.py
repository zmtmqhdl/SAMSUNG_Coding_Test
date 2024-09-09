import sys
input = sys.stdin.readline

N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def grow(x, y) :
    Empty = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N :
            if board[nx][ny] > 0 :
                board[x][y] += 1
            elif board[nx][ny] == 0 and not WeedKiller[nx][ny] :
                Empty.append((nx, ny))
    for i, j in Empty :
        TotalEmpty[(i, j)] = TotalEmpty.get((i, j), 0) + (board[x][y] // len(Empty))

def bleed(TotalEmpty) :
    for x, y in TotalEmpty :
        board[x][y] += TotalEmpty[(x, y)]

def check(x, y) :
    cnt = board[x][y]
    for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)] :
        nx, ny = x, y
        for _ in range(K) :
            nx, ny = nx + dx, ny + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0 :
                cnt += board[nx][ny]
            else :
                break
    TotalDeath.append((cnt, x, y))

def weed(x, y) :
    WeedKiller[x][y] = C
    board[x][y] = 0
    for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)] :
        nx, ny = x, y
        for _ in range(K) :
            nx, ny = nx + dx, ny + dy
            if 0 <= nx < N and 0 <= ny < N :
                WeedKiller[nx][ny] = C
                if board[nx][ny] > 0 :
                    board[nx][ny] = 0
                else :
                    break


WeedKiller = [[0] * N for _ in range(N)]
ans = 0

for m in range(M) :
    TotalEmpty = {}
    for x in range(N) :
        for y in range(N) :
            if board[x][y] > 0 :
                grow(x, y)
    bleed(TotalEmpty)
    TotalDeath = []
    for x in range(N) :
        for y in range(N) :
            if board[x][y] > 0 :
                check(x, y)
    if TotalDeath :
        TotalDeath.sort(key = lambda x : (-x[0], x[1], x[2]))
        ans += TotalDeath[0][0]
    for x in range(N) :
        for y in range(N) :
            if WeedKiller[x][y] :
                WeedKiller[x][y] -= 1
    if TotalDeath :
        weed(TotalDeath[0][1], TotalDeath[0][2])
print(ans)