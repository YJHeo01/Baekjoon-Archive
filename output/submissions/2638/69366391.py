def cheese(graph,n,m):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer = 0
    remove_v = []
    while 1:
        cheese_cnt = 0        
        for i in range(n):
            for j in range(m):
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
        for remove in remove_v:
            graph[remove[0]][remove[1]] = 0
        if cheese_cnt == 0:
            print(answer)
            return
        answer += 1

                    

    

n,m = map(int,input().split())

paper = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    paper.append(tmp)

cheese(paper,n,m)