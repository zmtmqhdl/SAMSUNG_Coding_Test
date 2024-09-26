def check() :
    for start in range(1, N + 1) : 
        s = start
        for i in range(1, H + 1) :
            if arr[i][s] == 1 : 
                s += 1
            elif arr[i][s - 1] == 1 : 
                s -= 1
        if s != start :
            return False
    return True

def dfs(n, s) :
    global ans
    if ans == 1 : 
        return
    if n == cnt : 
        if check() :
            ans = 1
        return
    for j in range(s, total_cnt) :
        x, y = pos[j]
        if arr[x][y - 1] == 0 and arr[x][y + 1] == 0 :
            arr[x][y] = 1
            dfs(n + 1, j + 1)
            arr[x][y] = 0

N, M, H = map(int, input().split())
arr = [[0] * (N + 2) for _ in range(H + 1)]
for _ in range(M) :
    x, y = map(int, input().split()) 
    arr[x][y] = 1
pos = []
for x in range(1, H + 1) :
    for y in range(1, N + 1) :
        if arr[x][y] == 0 and arr[x][y - 1] == 0 and arr[x][y + 1] == 0 :
            pos.append((x, y))
total_cnt = len(pos)

for cnt in range(4) :
    ans = 0
    dfs(0, 0)
    if ans == 1 :
        print(cnt)
        break
else :
    print(-1)
