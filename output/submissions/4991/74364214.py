from collections import deque
import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,-0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 'x':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

while True:
    w,h = map(int,input().split())
    if w == 0:
        break
    room = []
    node = []
    edges = []
    node_cnt = 0
    for i in range(h):
        tmp = list(input())
        room.append(tmp)
        for j in range(w):
            if tmp[j] == 'o' or tmp[j] == '*':
                node.append((i,j))
                node_cnt += 1
    for i in range(node_cnt-1):
        distance = [[INF]*w for _ in range(h)]
        bfs(room,distance,node[i])
        for j in range(i+1,node_cnt):
            heapq.heappush(edges,(distance[node[j][0]][node[j][1]],i,j))
    parent = [0] * node_cnt
    for i in range(1,node_cnt):
        parent[i] = i
    answer = 0
    while edges:
        dist, a, b = heapq.heappop(edges)
        if find_parent(parent,a) != find_parent(parent,b):
            if dist >= INF:
                answer = -1
                break
            union_parent(parent,a,b)
            answer += dist
    print(answer)
