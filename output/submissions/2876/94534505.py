import sys

input = sys.stdin.readline

n = int(input())

cnt = [[0]*2 for _ in range(6)]

for i in range(n):
    a,b = map(int,input().split())
    cnt[a][0] += 1
    cnt[b][1] += 1
    
student = []

for i in range(1,6):
    for j in range(2):
        student.append((cnt[i][j],i))
        
student.sort(key=lambda x:-x[0])

print(*student[0])