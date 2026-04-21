import sys

input = sys.stdin.readline

n = int(input())

tower = []

for _ in range(n):
    a,b = map(int,input().split())
    tower.append((a,b))

tower.sort()

tallest_tower = [0,0]
tallest_tower_idx = 0
answer = 0

for i in range(n):
    if tower[i][1] >= tallest_tower[1]:
        tallest_tower_idx = i
        answer += (tallest_tower[1]) * (tower[i][0]-tallest_tower[0])
        tallest_tower = tower[i]

answer += tallest_tower[1]
tallest_tower = [1001,0]

for i in range(n-1,tallest_tower_idx-1,-1):
    if tower[i][1] >= tallest_tower[1]:
        answer += (tallest_tower[1]) * (tallest_tower[0]-tower[i][0])
        tallest_tower = tower[i]

print(answer)