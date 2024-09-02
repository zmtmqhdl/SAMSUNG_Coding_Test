import sys
from collections import deque

chair = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
k = int(input())
moves = [list(map(int, input().split())) for _ in range(k)]
LEFT_INDEX, RIGHT_INDEX = 6, 2
for n, d in moves:
    n -= 1
    turn = [(n, d)]
    move = d
    for i in range(n - 1, -1, -1):
        if chair[i + 1][LEFT_INDEX] != chair[i][RIGHT_INDEX]:
            move *= -1
            turn.append((i, move))
        else :
            break
    move = d
    for i in range(n + 1, 4):
        if chair[i - 1][RIGHT_INDEX] != chair[i][LEFT_INDEX]:
            move *= -1
            turn.append((i, move))
        else:
            break
    for a, b in turn :
        chair[a].rotate(b)
result = sum([chair[i][0] * (1 << i) for i in range(4)])
print(result)