from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[[] for _ in range(3)] for _ in range(1001)]
size = [[0]*3 for _ in range(1001)]

graph[0][0].append([0,1,2*n,size[0][1]])
graph[0][1].append([0,0,0,size[0][0]])

size[0][1] += 1
size[0][0] += 1

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    graph[0][1].append([i,0,2,size[i][0]])
    graph[i][0].append([0,1,0,size[0][1]])
    size[i][0] += 1; size[0][1] += 1
    graph[i][0].append([i,1,2,size[i][1]])
    graph[i][1].append([i,0,0,size[i][0]])
    size[i][1] += 1; size[i][0] += 1
    if tmp[0] == 0: continue
    for j in tmp[1:]:
        graph[i][1].append([j,2,1,size[j][2]])
        graph[j][2].append([i,1,0,size[i][1]])
        size[i][1] += 1; size[j][2] += 1
    
for j in range(1,1001):
    graph[j][2].append([0,2,1,size[0][2]])
    graph[0][2].append([j,2,0,size[j][2]])
    size[0][2] += 1; size[j][2] += 1

answer = 0

def bfs(graph,parent):
    queue = deque([(0,0,int(1e9))])
    parent[0][0] = [0,0,0]
    while queue:
        x,y,flow = queue.popleft()
        for i in range(size[x][y]):
            nx,ny,cap,rev = graph[x][y][i]
            if parent[nx][ny] == [-1,-1,-1] and cap > 0:
                parent[nx][ny] = [x,y,i]
                next_flow = min(flow,cap)
                if nx == 0 and ny == 2: return next_flow
                queue.append((nx,ny,next_flow))
    return 0

while True:
    parent = [[[-1,-1,-1]]*3 for _ in range(1001)]
    tmp = bfs(graph,parent)
    if tmp == 0: break
    answer += tmp
    x,y = 0,2
    while True:
        if x == 0 and y == 0: break
        nx,ny,ni = parent[x][y]
        graph[nx][ny][ni][2] -= tmp
        rev = graph[nx][ny][ni][3]
        graph[x][y][rev][2] += tmp
        x,y = nx,ny
        
print(answer)