import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
atomics = []
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    atomics.append((x - 1, y - 1, m, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    grid = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(atomics)):
        x, y, m, s, d = atomics[i]
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        grid[nx][ny].append((m, s, d))
    return grid

def mix(grid):
    new_atomics = []
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) == 1:
                new_atomics.append((i, j) + grid[i][j][0])
            elif len(grid[i][j]) > 1:
                total_mass, total_speed, cnt = 0, 0, len(grid[i][j])
                even_directions, odd_directions = True, True
                for mass, speed, direction in grid[i][j]:
                    total_mass += mass
                    total_speed += speed
                    if direction % 2 == 0:
                        odd_directions = False
                    else:
                        even_directions = False
                new_mass = total_mass // 5
                if new_mass > 0:
                    new_speed = total_speed // cnt
                    if even_directions or odd_directions:
                        directions = [0, 2, 4, 6]
                    else:
                        directions = [1, 3, 5, 7]
                    for d in directions:
                        new_atomics.append((i, j, new_mass, new_speed, d))
    return new_atomics

for _ in range(K):
    grid = move()
    atomics = mix(grid)
ans = sum([i[2] for i in atomics])
print(ans)
