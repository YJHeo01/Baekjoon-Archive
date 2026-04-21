from collections import deque

t = int(input())

def solution():
    n,k = map(int,input().split())
    rule = [[]for _ in range(n+1)]
    indegree = [0] * (n+1)
    build_time = [0] + list(map(int,input().split()))
    for _ in range(k):
        a,b = map(int,input().split())
        rule[a].append(b)
        indegree[b] += 1
    dest = int(input())
    start = deque([])
    build_complete_time = [0] * (n+1)
    build_complete = [False] * (n+1)
    for i in range(1,n+1):
        if indegree[i] == 0:
            start.append(i)
    while start:
        building = start.popleft()
        build_complete[building] = True
        build_complete_time[building] += build_time[building]
        for next_build in rule[building]:
            if build_complete[next_build] == True:
                continue
            indegree[next_build] -= 1
            if indegree[next_build] == 0:
                start.append(next_build)
            build_complete_time[next_build] = max(build_complete_time[next_build],build_complete_time[building])
    print(build_complete_time[dest])
            
for _ in range(t):
    solution()