import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(n - 1, -1, -1) :
    if i + lst[i][0] <= n :
        dp[i] = max(dp[i + lst[i][0]] + lst[i][1], dp[i + 1])
    else :
        dp[i] = dp[i + 1]
print(dp[0])