import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
pieces = {}
direction = {}
pos = {}
for i in range(K):
    x, y, d = map(int, input().split())
    pos[i] = (x - 1, y - 1)
    direction[i] = d - 1
    if (x - 1, y - 1) not in pieces:
        pieces[(x - 1, y - 1)] = [i]
    else:
        pieces[(x - 1, y - 1)].append(i)

ans = 1

def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while True:
    for cur in range(K):
        x, y = pos[cur]
        idx = pieces[(x, y)].index(cur)
        d = direction[cur]
        nx, ny = x + dx[d], y + dy[d]

        if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == 2:
            d = change_direction(d)
            direction[cur] = d
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == 2:
                continue

        if arr[nx][ny] == 0:
            for i in pieces[(x, y)][idx:]:
                pos[i] = (nx, ny)
            pieces[(nx, ny)] = pieces.get((nx, ny), []) + pieces[(x, y)][idx:]
            pieces[(x, y)] = pieces[(x, y)][:idx]
        
        elif arr[nx][ny] == 1:
            for i in pieces[(x, y)][idx:]:
                pos[i] = (nx, ny)
            pieces[(nx, ny)] = pieces.get((nx, ny), []) + pieces[(x, y)][idx:][::-1]
            pieces[(x, y)] = pieces[(x, y)][:idx]
        
        if len(pieces[nx, ny]) >= 4:
            print(ans)
            exit()

    ans += 1
    if ans > 1000:
        print(-1)
        break
