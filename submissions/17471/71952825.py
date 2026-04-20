from collections import deque
from itertools import combinations

n = int(input())

town = [0] + list(map(int,input().split()))

graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    for j in range(1,tmp[0]+1):
        graph[i].append(tmp[j])

data = []

for i in range(1,n):
    data.append(i)

data.append(n)

def bfs(graph,elections):
    visited = [False] * (n+1)
    visited[elections[0]] = True
    queue = deque([elections[0]])
    tmp = 1
    while queue:
        election = queue.popleft()
        for next_election in graph[election]:
            if visited[next_election] == False and next_election in elections:
                visited[next_election] = True
                tmp += 1
                queue.append(next_election)
    if tmp == len(elections):
        return True
    return False
        

INF = int(1e9)

def gerrymandering(graph,election_A):
    election_B = []
    for i in range(1,n+1):
        if i not in election_A:
            election_B.append(i)
    if bfs(graph,election_A) == False or bfs(graph,election_B) == False:
        return INF
    value = 0
    for i in election_A:
        value += town[i]
    for i in election_B:
        value -= town[i]
    return abs(value)

answer = INF
for i in range(1,n//2+1):
    case_list = list(combinations(data,i))
    for case in case_list:
        answer = min(answer,gerrymandering(graph,case))

if answer == INF:
    answer = -1
print(answer)