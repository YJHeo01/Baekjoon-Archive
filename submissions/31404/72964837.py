h,w = map(int,input().split())

clean = [[False]*w for _ in range(h)]



r,c,d = map(int,input().split())

ruleA = []

for _ in range(h):
    ruleA.append(list(input()))

ruleB = []

for _ in range(h):
    ruleB.append(list(input()))

def solution(graphA,graphB,clean,start):
    visited = [[[False]*w for _ in range(h)]for _ in range(4)]
    ret_value = 0
    move_cnt = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    nx,ny,nd = start
    while True:
        vx,vy,d = nx,ny,nd
        move_cnt += 1
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            return ret_value
        if clean[vx][vy] == False:
            clean[vx][vy] = True
            visited = [[[False]*w for _ in range(h)]for _ in range(4)]
            nd = (d+int(graphA[vx][vy])) % 4
            ret_value = move_cnt
        else:
            nd = (d+int(graphB[vx][vy])) % 4
            if visited[nd][vx][vy] == True:
                return ret_value
            visited[nd][vx][vy] = True
        nx = vx + dx[nd]
        ny = vy + dy[nd]

print(solution(ruleA,ruleB,clean,(r,c,d)))