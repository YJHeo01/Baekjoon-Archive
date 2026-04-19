import sys

input = sys.stdin.readline

start = []
end = []

n,m = map(int,input().split())

for _ in range(n):
    tmp = list(map(int,input().split()))
    start.append(tmp[1])
    end.append(tmp[-1])

answer = 0

distance = int(1e18)

for i in range(1,m+1):
    tmp = 0
    for j in range(n):
        tmp += abs(i-start[j])
        tmp += abs(i-end[j])
    if distance > tmp:
        answer = i
        distance = tmp

print(answer)