import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
R -= 1
C -= 1
board = [list(map(int, input().split())) for _ in range(3)]
ans = 0

def change(lst, l) :
    new_board = []
    zero_len = 0
    for i in range(l) :
        tmp = []
        for j in set(sorted(lst[i], key = lambda x : (lst[i].count(x), x))) :
            if j != 0 :
                tmp += [j, lst[i].count(j)]
        new_board.append(tmp)
        zero_len = max(zero_len, len(tmp))
    new_board = zero(new_board, zero_len)
    return new_board

def zero(lst, l) :
    for i in range(len(lst)) :
        lst[i] += [0] * (l - len(lst[i]))
    return lst


while True :
    if ans > 100 :
        print(-1)
        break
    N, M = len(board), max([len(i) for i in board])
    if R <= N - 1 and C <= M - 1 :
        if board[R][C] == K :
            print(ans)
            break
    if N >= M :
        board = change(board, N)
    else :
        board = change(list(map(list, zip(*board))), M)
        for _ in range(3) :
            board = list(map(list, zip(*board)))
    ans += 1
