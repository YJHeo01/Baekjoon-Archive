import sys

input = sys.stdin.readline

r,c = map(int,input().split())
room = [[0]*c for _ in range(r)]
k = int(input())
for _ in range(k):
    br,bc = map(int,input().split())
    room[br][bc] = 1
sr,sc = map(int,input().split())
command = list(map(int,input().split()))
visited = [[False]*c for _ in range(r)]

def solution(graph,visited,start):
    vx,vy,d = start
    dx = [0,-1,1,0,0]
    dy = [0,0,0,-1,1]
    visited[vx][vy] = True
    while True:
        for i in range(4):
            next_d = command[(d+i) % 4] 
            nx = vx + dx[next_d]
            ny = vy + dy[next_d]
            if nx < 0 or ny < 0 or nx >= r or ny >=c or visited[nx][ny] == True or graph[nx][ny] == 1:
                if i == 3:
                    return (vx,vy)
                continue
            visited[nx][ny] = True
            vx,vy,d = nx,ny,(d+i)%4
            break
answer = solution(room,visited,(sr,sc,0))

for i in answer:
    print(i,end=" ")
