import sys
input = sys.stdin.readline

def clean():
    x1, y1 = dust[0]
    x2, y2 = dust[1]

    for x in range(x1 - 1, 0, -1):
        board[x][0] = board[x-1][0]
    for y in range(M - 1):
        board[0][y] = board[0][y+1]
    for x in range(x1):
        board[x][M-1] = board[x+1][M-1]
    for y in range(M - 1, 1, -1):
        board[x1][y] = board[x1][y-1]

    for x in range(x2 + 1, N - 1):
        board[x][0] = board[x+1][0]
    for y in range(M - 1):
        board[N-1][y] = board[N-1][y+1]
    for x in range(N - 1, x2, -1):
        board[x][M-1] = board[x-1][M-1]
    for y in range(M - 1, 1, -1):
        board[x2][y] = board[x2][y-1]
        
    board[x1][1] = board[x2][1] = 0

def spread():
    new_board = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if board[x][y] > 0:
                amount = board[x][y] // 5
                count = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != -1:
                        new_board[nx][ny] += amount
                        count += 1
                new_board[x][y] += board[x][y] - amount * count
            elif board[x][y] == -1:
                new_board[x][y] = -1
    return new_board

def total():
    return sum(sum(row) for row in board) + 2

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dust = [(i, 0) for i in range(N) if board[i][0] == -1]

for _ in range(T):
    board = spread()
    clean()

print(total())
