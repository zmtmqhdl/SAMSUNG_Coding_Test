import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
order = []
for _ in range(m) :
    d, p = map(int, input().split())
    order.append([d - 1, p])
tonic = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]

dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]

for d, p in order :
    next_tonic = []
    use_tonic = []
    for x, y in tonic :
        nx, ny = (x + dx[d] * p) % n, (y + dy[d] * p) % n
        use_tonic.append([nx, ny])

    for x, y in use_tonic :
        board[x][y] += 1
    
    for x, y in use_tonic :
        for i in [1, 3, 5, 7] :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] >= 1 :
                board[x][y] += 1
    
    for x in range(n) :
        for y in range(n) :
            if board[x][y] >= 2 and [x, y] not in use_tonic :
                board[x][y] -= 2
                next_tonic.append([x, y])

    tonic = next_tonic


ans = 0
for x in range(n) :
    for y in range(n) :
        ans += board[x][y]
print(ans)