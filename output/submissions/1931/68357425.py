import sys
input = sys.stdin.readline
n = int(input())

plan = []

for i in range(n):
    a,b= map(int,input().split())
    plan.append((a,b))

plan = sorted(plan, key = lambda x : (x[1],x[0]))

cnt = 1
index = 0
for i in range(1,n):
    if plan[i][0] >= plan[index][1]:
        cnt += 1
        index = i

print(cnt)