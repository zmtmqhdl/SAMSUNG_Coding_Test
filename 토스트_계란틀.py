import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True :
    visit = [[False] * N for _ in range(N)]
    change = False
    for i in range(N) :
        for j in range(N) :
            if not visit[i][j] :
                q = deque([(i, j)])
                visit[i][j] = True
                total = 0
                egg = []
                while q :
                    x, y = q.popleft()
                    egg.append((x, y))
                    total += board[x][y]
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and L <= abs(board[x][y] - board[nx][ny]) <= R :
                            change = True
                            visit[nx][ny] = True
                            q.append((nx, ny))
                total = int(total / len(egg))
                for x, y in egg :
                    board[x][y] = total
    if change :
        ans += 1
    else :
        print(ans)
        break