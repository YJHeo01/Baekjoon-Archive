import sys

input = sys.stdin.readline

n,k = map(int,input().split())

INF = int(1e9)

arr = [list(map(int,input().split())) for _ in range(n)]

start = [[] for _ in range(k)]

answer = 0
answer_dist = INF

s, target_x, target_y = map(int,input().split())
target_x -= 1; target_y -= 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0: continue
        dist = abs(i-target_x) + abs(j-target_y)
        if dist <= s and (answer_dist > dist or (answer_dist == dist and arr[i][j] < answer)):
            answer = arr[i][j]
            answer_dist = dist

print(answer)