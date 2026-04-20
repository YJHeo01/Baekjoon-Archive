from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

name = []

stat = []

for i in range(n):
    c,p,a,s = input().split()
    name.append(c)
    stat.append([int(p),int(a),int(s)])
    
graph = [[] for _ in range(n)]

indegree = [0] * n

for i in range(n):
    for j in range(i):
        a_win = 0
        b_win = 0
        for k in range(3):
            if stat[i][k] >= stat[j][k]: a_win+=1
            if stat[j][k] >= stat[i][k]: b_win+=1
        if a_win > b_win:
            graph[i].append(j)
            indegree[j] += 1
        if b_win > a_win:
            graph[j].append(i)
            indegree[i]+=1

Paradoxe_Absurdo = False

queue = deque([])

answer = []

for i in range(n):
    if indegree[i] == 0:
        answer.append(name[i])

answer.sort()

for i in range(n):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            queue.append(nx)

if sum(indegree) != 0: Paradoxe_Absurdo = True

if Paradoxe_Absurdo:
    print("Paradoxe Absurdo")
else:
    for i in answer:
        print(i)