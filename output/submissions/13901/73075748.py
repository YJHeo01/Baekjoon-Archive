import sys

input = sys.stdin.readline

r,c = map(int,input().split())
k = int(input())
impossible_move = [[False]*c for _ in range(r)]
for _ in range(k):
    br,bc = map(int,input().split())
    impossible_move[br][bc] = True
sr,sc = map(int,input().split())
command = list(map(int,input().split()))


def solution(visited,start):
    vx,vy,d = start
    dx = [0,-1,1,0,0]
    dy = [0,0,0,-1,1]
    visited[vx][vy] = True
    while True:
        for i in range(4):
            next_d = command[(d+i) % 4] 
            nx = vx + dx[next_d]
            ny = vy + dy[next_d]
            if nx < 0 or ny < 0 or nx >= r or ny >=c or visited[nx][ny] == True:
                if i == 3:
                    return (vx,vy)
                continue
            visited[nx][ny] = True
            vx,vy,d = nx,ny,(d+i)%4
            break
answer = solution(impossible_move,(sr,sc,0))

for i in answer:
    print(i,end=" ")
