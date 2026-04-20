import sys

input = sys.stdin.readline

start = []
end = []

n,m = map(int,input().split())

pos = [0] * (m+1)

for _ in range(n):
    tmp = list(map(int,input().split()))
    pos[tmp[1]] += 1
    pos[tmp[-1]] += 1

answer = 0

min_distance = 0

for i in range(m+1):
    min_distance += pos[i] * i

left_cnt = 0
right_cnt = 2 * n

tmp_distance = min_distance

for i in range(1,m+1):
    tmp_distance -= right_cnt
    right_cnt -= pos[i]
    tmp_distance += left_cnt
    if min_distance > tmp_distance:
        answer = i
        min_distance = tmp_distance
    left_cnt += pos[i]
    
print(answer)