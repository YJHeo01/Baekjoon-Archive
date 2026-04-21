from collections import deque

a,b,c = map(int,input().split())

max_value = max(a,b,c)
visited = [[[False]*(max_value+1) for _ in range(max_value+1)] for _ in range(max_value+1)]

answer = [False] * (c+1)
size = [a,b,c]

def solution(size,visited,answer):
    answer[size[2]] = True
    queue = deque([[0,0,size[2]]])
    visited[0][0][size[2]] = True
    while queue:
        va, vb, vc = queue.popleft()
        water = [va,vb,vc]
        if va == 0:
            answer[vc] = True
        for i in range(3):
            if water[i] == 0:
                continue
            for j in range(3):
                if i == j:
                    continue
                next_water = [va,vb,vc]
                if water[i] + water[j] > size[j]:
                    next_water[j] = size[j]
                    next_water[i] = water[i] + water[j] - size[j]
                else:
                    next_water[j] = water[i] + water[j]
                    next_water[i] = 0
                na,nb,nc = next_water
                if visited[na][nb][nc] == False:
                    visited[na][nb][nc] = True
                    queue.append(next_water)
        
solution(size,visited,answer)

for i in range(c+1):
    if answer[i] == True:
        print(i,end=" ")