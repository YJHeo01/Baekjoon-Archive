import sys
input = sys.stdin.readline

n,m = map(int,input().split())

meat_list = []

for _ in range(n):
    a,b = map(int,input().split())
    meat_list.append((b,a))
meat_list.sort()
answer = -1
value_sum = 0
for i in range(n):
    value_sum += meat_list[i][1]
    if value_sum >= m:
        answer = meat_list[i][0]
        break

print(answer)