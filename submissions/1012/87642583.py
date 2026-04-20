#질문게시판 답안용

from collections import deque
import sys
input  = sys.stdin.readline
t = int(input())

dy = [-1,1,0,0] # 행   위 , 아래, 고정 , 고정
dx = [0,0,-1,1] # 열  고정, 고정, 왼쪽 , 오른쪽

def bfs(graph,y,x): 
    q = deque([(y,x)]) ## 덱 사용, x,y 와 y,x 순서 통일하셔야 합니다. 
    graph[y][x] = 0 # 입력받은 좌표 값 변경(배추제거  1 -> 0)
    while q:
        y,x = q.popleft() ## 
        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n: continue ## 범위 벗어났는지 판별별
            if graph[ny][nx] == 1: # 배추가 있으면 
                    q.append((ny,nx)) # 큐에 좌표를 추가하고
                    graph[ny][nx] = 0 # 방문처리
            else:
                continue
for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0]*(m+1) for _ in range(n+1)] 
    cnt = 0
    for _ in range(k):
        x,y = map(int, input().split())
        #x = x + 1
        #y = y + 1 ## 문제에서 주어지는 범위는 0 <= x,y < n,m이므로 굳이 변형 필요 x
        graph[y][x] = 1

    for y in range(n): ##문제에서 주어지는 범위는 0 <= x,y < n,m
        for x in range(m): 
            if graph[y][x] == 1: 
                bfs(graph, y,x) #y와 i는 세로축을, x와 j는 가로축을 나타냄
                cnt +=1

    print(cnt)