import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
global ans
ans = 1e9
def dfs(num, arr1, arr2):
    global ans
    if num == n :
        if len(arr1) == len(arr2) :
            sum1, sum2 = 0, 0
            for i in range(n // 2) :
                for j in range(n // 2) :
                    sum1 += board[arr1[i]][arr1[j]]
                    sum2 += board[arr2[i]][arr2[j]]
            ans = min(ans, abs(sum1 - sum2))
        return
    if len(arr1) < n // 2 :
        dfs(num + 1, arr1 + [num], arr2)
    if len(arr2) < n // 2 :
        dfs(num + 1, arr1, arr2 + [num])
dfs(0, [], [])
print(ans)