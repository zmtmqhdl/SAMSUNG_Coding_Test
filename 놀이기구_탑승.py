import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * n for _ in range(n)]
students = {}
for _ in range(n ** 2) :
    tmp = list(map(int, input().split()))
    students[tmp[0]] = tmp[1:]
score = [0, 1, 10, 100, 1000]
ans = 0
for student in students :
    check = []
    for x in range(n) :
        for y in range(n) :
            like, empty = 0, 0
            if not board[x][y] :
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) :
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n :
                        if board[nx][ny] in students[student] :
                            like += 1
                        if not board[nx][ny] :
                            empty += 1
            check.append((like, empty, x, y))
    check.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    for a, b, i, j in check :
        if not board[i][j] :
            board[i][j] = student
            break

for x in range(n) :
    for y in range(n) :
        cnt = 0
        student = board[x][y]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) :
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in students[student] :
                    cnt += 1
        ans += score[cnt]
print(ans)