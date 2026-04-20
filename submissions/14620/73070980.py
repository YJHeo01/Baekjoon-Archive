n = int(input())

ground = []

for _ in range(n):
    ground.append(list(map(int,input().split())))
flower1_visited = [[False]*n for _ in range(n)]
flower2_visited = [[False]*n for _ in range(n)]
INF = int(1e9)
def get_price(flower_A,flower_B,flower_C):
    ret_value = 0
    A_vx, A_vy = flower_A
    B_vx, B_vy = flower_B
    C_vx, C_vy = flower_C
    dx = [0,1,0,-1,0]
    dy = [1,0,-1,0,0]
    for i in range(5):
        A_nx = A_vx + dx[i]
        B_nx = B_vx + dx[i]
        C_nx = C_vx + dx[i]
        A_ny = A_vy + dy[i]
        B_ny = B_vy + dy[i]
        C_ny = C_vy + dy[i]
        ret_value += (ground[A_nx][A_ny]+ground[B_nx][B_ny]+ground[C_nx][C_ny])
    return ret_value

def dead_flower(flower_A,flower_B):
    graph = [[False]*n for _ in range(n)]
    dx = [0,0,1,0,-1]
    dy = [0,-1,0,1,0]
    vx,vy = flower_A
    for i in range(5):
        nx = vx + dx[i]
        ny = vy + dy[i]
        graph[nx][ny] = True
    vx,vy = flower_B
    for i in range(5):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if graph[nx][ny] == True:
            return False
    return True
answer = INF
for flower1_x in range(1,n-1):
    for flower1_y in range(1,n-1):
        flower1_visited[flower1_x][flower1_y] = True
        for flower2_x in range(1,n-1):
            for flower2_y in range(1,n-1):
                if dead_flower((flower1_x,flower1_y),(flower2_x,flower2_y)) == True:
                    continue
                if flower1_visited[flower2_x][flower2_y] == True:
                    continue
                flower2_visited[flower2_x][flower2_y] = True
                for flower3_x in range(1,n-1):
                    for flower3_y in range(1,n-1):
                        if dead_flower((flower3_x,flower3_y),(flower2_x,flower2_y)) == True or dead_flower((flower1_x,flower1_y),(flower3_x,flower3_y)) == True:
                            continue
                        if flower2_visited[flower3_x][flower3_y] == True:
                            continue
                        answer = min(answer,get_price((flower1_x,flower1_y),(flower2_x,flower2_y),(flower3_x,flower3_y)))

print(answer)
                        