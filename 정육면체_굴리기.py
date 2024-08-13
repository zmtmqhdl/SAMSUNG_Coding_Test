n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move_dt = list(map(int, input().split()))
move = {1 : (0, 1), 2 : (0, -1), 3 : (-1, 0), 4 : (1, 0)}
dice = {1 : board[x][y], 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
board[x][y] = 0
for i in move_dt :
    dx, dy = move[i]
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m :
        x, y = nx, ny
        if i == 1 : # 동
            dice[5], dice[2], dice[6], dice[4] = dice[2], dice[6], dice[4], dice[5]
        elif i == 2 : # 서
            dice[5], dice[2], dice[6], dice[4] = dice[4], dice[5], dice[2], dice[6]
        elif i == 3 : # 북
            dice[1], dice[2], dice[3], dice[4] = dice[4], dice[1], dice[2], dice[3]
        elif i == 4 : # 남
            dice[1], dice[2], dice[3], dice[4] = dice[2], dice[3], dice[4], dice[1]
        print(dice[4])
        if board[x][y] != 0 :
            dice[2] = board[x][y]
            board[x][y] = 0
        else :
            board[x][y] = dice[2]