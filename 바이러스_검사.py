n = int(input())
dt = list(map(int, input().split()))
a, b = map(int, input().split())
ans = 0
for i in dt :
    if i - a < 0 :
        ans += 1
    elif (i - a) % b == 0 :
        ans += (i - a) // b + 1
    elif (i - a) % b :
        ans += (i - a) // b + 2
print(ans)