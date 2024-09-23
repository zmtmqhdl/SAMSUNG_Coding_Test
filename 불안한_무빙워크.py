import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
q = deque([[i, 0] for i in map(int, input().split())])
ans, stop = 0, 0
while stop < K :
    ans += 1
    q.rotate(1)
    for i in range(N - 1, -1, -1) :
        if i == N - 1 :
            if q[i][1] :
                q[i][1] = 0
        elif i == N - 2 and q[i][1] and not q[i + 1][1] and q[i + 1][0]:
            if q[i + 1][0] :
                q[i][1] = 0
                q[i + 1][0] -= 1
                if not q[i + 1][0] :
                    stop += 1
        elif i == 0 :
            if q[i][0] and not q[i][1] :
                q[i][1] = 1
                q[i][0] -= 1
                if not q[i][0] :
                    stop += 1
        else :
            if q[i][1] and not q[i + 1][1] and q[i + 1][0] :
                q[i][1] = 0
                q[i + 1][1] = 1
                q[i + 1][0] -= 1
                if not q[i + 1][0] :
                    stop += 1
print(ans)
