import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 1
board[x][y] = 2
direciton = {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}
while True :
    moved = False
    for _ in range(4) :
        nd = (d + 3) % 4
        nx, ny = x + direciton[nd][0], y + direciton[nd][1]
        if board[nx][ny] == 0 :
            board[nx][ny] = 2
            x, y = nx, ny
            d = nd
            ans += 1
            moved = True
            break
        else:
            d = nd
    if not moved :
        nx, ny = x - direciton[d][0], y - direciton[d][1]
        if board[nx][ny] != 1 :
            x, y = nx, ny
        else:
            break
print(ans)
