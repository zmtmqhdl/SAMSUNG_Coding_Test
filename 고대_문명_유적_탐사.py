import sys
from copy import deepcopy
from collections import deque

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
artifact = list(map(int, input().split()))

ans = []

def rotate(arr, x, y) :
    narr = [i[:] for i in arr]
    for i in range(3) :
        for j in range(3) :
            narr[x+i][y+j]=arr[x+3-j-1][y+i]
    return narr

def get_score(arr, mode) :
    visit = [[False] * 5 for _ in range(5)]
    total = 0
    for i in range(5) :
        for j in range(5) :
            tmp = bfs(arr, visit, i, j, mode)
            total += tmp
    return total

def bfs(arr, visit, i, j, mode) :
    q = deque([(i, j)])
    cnt = 1
    visit[i][j] = True
    get = [(i, j)]
    while q :
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visit[nx][ny] and arr[nx][ny] == arr[i][j] :
                visit[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
                get.append((nx, ny))
    if cnt >= 3 :
        if mode :
            for i, j in get :
                arr[i][j] = 0
        return cnt
    else :
        return 0

for _ in range(K) :
    max_score = 0
    for angle in range(1, 4) :
        for y in range(3) :
            for x in range(3) :
                narr = [i[:] for i in arr]
                for _ in range(angle) :
                    narr = rotate(narr, x, y)
                score = get_score(narr, 0)
                if max_score < score :
                    max_score = score
                    marr = narr
    if not max_score :
        break
    total_score = 0
    arr = marr
    while True :
        score = get_score(arr, 1)
        if not score :
            break
        total_score += score
        for y in range(5) :
            for x in range(4, -1, -1) :
                if arr[x][y] == 0 :
                    arr[x][y] = artifact.pop(0)
    ans.append(total_score)
print(*ans)