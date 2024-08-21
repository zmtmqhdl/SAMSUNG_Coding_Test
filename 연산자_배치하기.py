import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
add, sub, mul = map(int, input().split())
max_num, min_num = -1e9, 1e9

def dfs(cnt, cur, add, sub, mul) :
    global max_num, min_num
    if cur < int(-1e9) or int(1e9) < cur :
        return
    if cnt == n :
        min_num = min(min_num, cur)
        max_num = max(max_num, cur)
        return
    if add > 0 :
        dfs(cnt + 1, cur + lst[cnt], add - 1, sub, mul)
    if sub > 0 :
        dfs(cnt + 1, cur - lst[cnt], add, sub - 1, mul)
    if mul > 0 :
        dfs(cnt + 1, cur * lst[cnt], add, sub, mul - 1)
dfs(1, lst[0], add, sub, mul)
print(int(min_num), int(max_num))