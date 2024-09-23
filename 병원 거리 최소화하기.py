import sys
input = sys.stdin.readline

def calculate_total_distance(selected_hospitals):
    total_distance = 0
    for person in peoples:
        min_distance = 1e9
        for hospital_idx in selected_hospitals:
            hx, hy = hospitals[hospital_idx]
            min_distance = min(min_distance, abs(person[0] - hx) + abs(person[1] - hy))
        total_distance += min_distance
    return total_distance

def select_hospital(idx, selected) :
    global min_total_distance
    if len(selected) == M:
        total_distance = calculate_total_distance(selected)
        min_total_distance = min(min_total_distance, total_distance)
        return
    if idx >= len(hospitals) :
        return
    select_hospital(idx + 1, selected + [idx])
    select_hospital(idx + 1, selected)

N, M = map(int, input().split())
board = []
peoples = []
hospitals = []
for x in range(N):
    row = list(map(int, input().split()))
    for y in range(N):
        if row[y] == 1:
            peoples.append((x, y))
        elif row[y] == 2:
            hospitals.append((x, y))
min_total_distance = 1e9
select_hospital(0, [])
print(min_total_distance)
