import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())
board = [[0] * 101 for _ in range(101)]

for _ in range(N) :
    x, y, d, g = map(int, input().split())
    board[x][y] = 1
    curve = [d]
    for _ in range(g) :
        for j in range(len(curve) - 1, -1, -1) :
            curve.append((curve[j] + 1) % 4)
    for i in range(len(curve)) :
        x += dx[curve[i]]
        y += dy[curve[i]]
        if 0 <= x < 101 and 0 <= y < 101 :
            board[x][y] = 1
            
ans = 0
for x in range(100) :
    for y in range(100) :
        if board[x][y] and board[x + 1][y] and board[x][y + 1] and board[x + 1][y + 1] :
            ans += 1
print(ans)
