from collections import deque

h,w = map(int,input().split())

r,c,d = map(int,input().split())

rule_A,rule_B = [],[]

for _ in range(h):
    rule_A.append(list(input()))
for _ in range(h):
    rule_B.append(list(input()))

clean_zone = [[False]*w for _ in range(h)]
visited = [[[False]*w for _ in range(h)]for _ in range(4)]

def solution(graph_A,graph_B,clean_zone,visited,start):
    ret_value = 0
    queue = deque([start])
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        vx,vy,direction,move_cnt = queue.popleft()
        if visited[direction][vx][vy] == True:
            return ret_value
        move_cnt += 1
        if clean_zone[vx][vy] == False:
            clean_zone[vx][vy] = True
            ret_value = move_cnt
            next_d = (direction+int(graph_A[vx][vy])) % 4
        else:
            visited[direction][vx][vy] = True
            next_d = (direction+int(graph_B[vx][vy])) % 4
        nx = vx + dx[next_d]
        ny = vy + dy[next_d]
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            return ret_value
        queue.append((nx,ny,next_d,move_cnt))
    return ret_value
            

print(solution(rule_A,rule_B,clean_zone,visited,(r,c,d,0)))