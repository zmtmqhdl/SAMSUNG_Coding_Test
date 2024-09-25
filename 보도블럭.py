N, L = map(int, input().split())
total_arr = [list(map(int, input().split())) for _ in range(N)]

for y in range(N) :
    total_arr.append([total_arr[x][y] for x in range(N)])

ans = 0

for arr in total_arr :
    cur = arr[0]
    used = [False] * N
    for i in range(1, N) :
        if arr[i] == cur :
            continue
        elif arr[i] - cur == 1 :
            if i - L < 0 :
                break
            for j in range(1, L + 1) :
                if arr[i - j] != cur or used[i - j] :
                    break
            else :
                for j in range(1, L + 1) :
                    used[i - j] = True
                cur = arr[i]
                continue
            break
        elif cur - arr[i] == 1 :
            if i + L - 1 >= N :
                break
            for j in range(L) :
                if arr[i + j] != arr[i] or used[i + j] :
                    break
            else :
                for j in range(L) :
                    used[i + j] = True
                cur = arr[i]
                continue
            break
        else :
            break
    else :
        ans += 1

print(ans)
