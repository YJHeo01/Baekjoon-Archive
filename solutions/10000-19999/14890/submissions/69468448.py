n, l = map(int,input().split())
ground = []

def search_road_h(idx,l):
    down = [[0] * n for _ in range(n)]
    up = [[0] * n for _ in range(n)]
    i = 0
    while i < (n-1):
        if ground[i][idx] == ground[i+1][idx]:
            i += 1
        elif ground[i][idx] + 1 == ground[i+1][idx]:
            for j in range(i,i-l,-1):
                 if j < 0:
                     return 0
                 elif ground[j][idx]+1 != ground[i+1][idx] or down[j][idx] == 1:
                     return 0
                 else:
                     up[j][idx] = 1
            i += 1
        elif ground[i][idx] == ground[i+1][idx]+1:
            for j in range(i+1,i+l+1):
                 if j >= n:
                     return 0
                 elif ground[i][idx] != ground[j][idx]+1 or up[j][idx] == 1:
                     return 0
                 else:
                     down[j][idx] = 1
            i += 1
        else:
            return 0
    return 1

def search_road_w(idx,l):
    up = [[0] * n for _ in range(n)]
    down = [[0] * n for _ in range(n)] 
    i = 0
    while i < (n-1):
        if ground[idx][i] == ground[idx][i+1]:
            i += 1
        elif ground[idx][i] + 1 == ground[idx][i+1]:
            for j in range(i,i-l,-1):
                 if j < 0:
                     return 0
                 elif ground[idx][j]+1 != ground[idx][i+1] or down[idx][j] == 1:
                     return 0
                 else:
                     up[idx][j] = 1
            i += 1
        elif ground[idx][i] == ground[idx][i+1]+1:
            for j in range(i+1,i+l+1):
                 if j >= n:
                     return 0
                 elif ground[idx][i] != ground[idx][j]+1 or up[idx][j] == 1:
                     return 0
                 else:
                     down[idx][j] = 1

            i += 1
        else:
            return 0
    return 1
        
                

for _ in range(n):
    tmp = list(map(int,input().split()))
    ground.append(tmp)

answer  = 0
for i in range(n):
    answer += search_road_w(i,l)

for i in range(n):
    answer += search_road_h(i,l)

print(answer)