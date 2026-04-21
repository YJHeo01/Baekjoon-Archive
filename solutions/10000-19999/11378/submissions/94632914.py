from collections import deque

import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [[]for _ in range(4001)]

cnt = [0] * 4001

graph[0].append([1,n+k,0])
graph[1].append([0,0,0])

cnt[0] += 1
cnt[1] += 1

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    graph[1].append([4*i,tmp[0],cnt[4*i]])
    graph[i*4].append([1,0,cnt[1]]) #원점 - 정점
    cnt[1] += 1
    cnt[4*i] += 1
    #max_flow[0][1][i][0] = tmp[0]
    graph[4*i].append([4*i+1,k+1,cnt[4*i+1]])
    graph[4*i+1].append([4*i,0,cnt[4*i]])
    cnt[4*i] += 1
    cnt[4*i+1] += 1
    #max_flow[i][0][i][1] = k + 1 #정점 분할(직원원)
    for j in tmp[1:]:
        graph[4*i+1].append([4*j+2,1,cnt[4*j+2]])
        graph[4*j+2].append([4*i+1,0,cnt[4*i+1]])
        cnt[4*j+2] += 1
        cnt[4*i+1] += 1
    #    max_flow[i][1][j][2] = 1 #직원 - 일 연결

for j in range(1,m+1):
    graph[4*j+2].append([4*j+3,1,cnt[4*j+3]])
    graph[4*j+3].append([4*j+2,0,cnt[4*j+2]])
    cnt[4*j+3] += 1
    cnt[4*j+2] += 1
    #max_flow[j][2][j][3] = 1 #정점 분할(일)
    graph[4*j+3].append([2,1,cnt[2]])
    graph[2].append([4*j+3,0,cnt[4*j+3]])
    cnt[4*j+3] += 1
    cnt[2] += 1
    #max_flow[j][3][0][2] = 1 #일 - 종착지 연결
    
graph[2].append([3,m,cnt[3]])
graph[3].append([2,0,cnt[2]])
#max_flow[0][2][0][3] = m #종착지 정점 분할

answer = 0

while True:
    prev = [(-1,-1)]*4001
    queue = deque([0])
    while queue and prev[3] == (-1,-1):
        x = queue.popleft()
        for i, (nx, cap, rev) in enumerate(graph[x]):
            if cap and prev[nx] == (-1,-1):
                queue.append(nx)
                prev[nx] = (x,i)
    if prev[3] == (-1,-1): break
    flow = n+m+k
    cur_x = 3
    while True:
        if cur_x == 0: break
        prev_x, i = prev[cur_x]
        flow = min(flow,graph[prev_x][i][1])
        cur_x = prev_x
    cur_x = 3
    answer += flow
    while True:
        if cur_x == 0: break
        prev_x, i = prev[cur_x]
        rev = graph[prev_x][i][2]
        graph[prev_x][i][1] -= flow
        graph[cur_x][rev][1] += flow
        cur_x= prev_x
        
print(answer)