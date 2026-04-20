def cheese(graph,n,m):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer = 0
    while 1:
        remove_v = []
        cheese_cnt = 0        
        for i in range(1,n-1):
            for j in range(1,m-1):
                if graph[i][j] == 1:
                    cheese_cnt += 1
                    cnt = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if graph[nx][ny] == 0:
                            cnt += 1
                    if cnt >= 2:
                        remove_v.append((i,j))
        if cheese_cnt == 0:
            print(answer)
            return
        for remove in remove_v:
            graph[remove[0]][remove[1]] = 0
        answer += 1

                    

    

n,m = map(int,input().split())

paper = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    paper.append(tmp)

cheese(paper,n,m)