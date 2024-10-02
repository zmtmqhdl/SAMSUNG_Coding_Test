dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, M, K = map(int, input().split())
molds = []
for _ in range(K) :
    x, y, s, d, b = map(int, input().split())
    molds.append((x - 1, y - 1, s, d - 1, b))

ans = 0
    
for col in range(M) :
    molds.sort(key=lambda x : (x[1], x[0]))
    for i in range(len(molds)) :
        if molds[i][1] == col :
            ans += molds[i][4]
            molds.pop(i)
            break
    new_board = [[[] for _ in range(M)] for _ in range(N)]
    for mold in molds :
        x, y, s, d, b = mold
        for _ in range(s) :
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < N and 0 <= ny < M) :
                if d == 0 :
                    d = 1
                elif d == 1 :
                    d = 0
                elif d == 2 :
                    d = 3
                elif d == 3 :
                    d = 2
                nx, ny = x + dx[d], y + dy[d]
            x, y = nx, ny
        new_board[x][y].append((s, d, b))

    new_molds = []
    for i in range(N) :
        for j in range(M) :
            if len(new_board[i][j]) > 1 :
                largest_mold = max(new_board[i][j], key = lambda x: x[2])
                new_molds.append((i, j, largest_mold[0], largest_mold[1], largest_mold[2]))
            elif len(new_board[i][j]) == 1 :
                new_molds.append((i, j, new_board[i][j][0][0], new_board[i][j][0][1], new_board[i][j][0][2]))
    molds = new_molds

print(ans)
