from collections import deque

N = int(input())
arr = []
for x in range(N) :
    tarr = list(map(int, input().split()))
    for y in range(N) :
        if tarr[y] == 9 :
            robotx, roboty = x, y
            tarr[y] = 0
    arr.append(tarr)
level, cnt = 2, 2

def distance() :
    monster = {}
    dis = [[1e9] * N for _ in range(N)]
    dis[robotx][roboty] = 0
    q = deque([(robotx, roboty)])
    while q :
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N :
                if arr[nx][ny] <= level and dis[x][y] + 1 < dis[nx][ny] :
                    dis[nx][ny] = dis[x][y] + 1
                    q.append((nx, ny))
                    if 0 < arr[nx][ny] < level :
                        monster[(nx, ny)] = min(monster.get((nx, ny), 1e9), dis[nx][ny])
    if monster : 
        return sorted([(monster[i], i[0], i[1]) for i in monster], key = lambda x : (x[0], x[1], x[2]))
    else :
        return []

ans = 0
while True :
    monster = distance()
    if monster :
        d, x, y = monster[0]
        arr[x][y] = 0
        cnt -= 1
        if cnt == 0 :
            level += 1
            cnt = level
        robotx, roboty = x, y
        ans += d
    else :
        print(ans)
        break
