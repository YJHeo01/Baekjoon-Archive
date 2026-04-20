n,l,r = map(int,input().split())

def people_move(graph,visited):
    value_sum = 0
    united_country_cnt = 0
    united_country = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                value = abs(graph[nx][ny]-graph[x][y])
                if value < l or value > r:
                    continue
                if visited[x][y] == 0:
                    visited[x][y] = 1
                    value_sum += graph[x][y]
                    united_country_cnt += 1
                    united_country.append((x,y))
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    value_sum += graph[nx][ny]
                    united_country_cnt += 1
                    united_country.append((nx,ny))
    if value_sum == 0:
        return 999
    next_value = value_sum // united_country_cnt
    for country in united_country:
        graph[country[0]][country[1]] = next_value
    return 1


country = []

for _ in range(n):
    tmp = list(map(int,input().split()))
    country.append(tmp)
answer = 0
finish = 0
while 1:
    visited = [[0]*n for _ in range(n)]
    finish = people_move(country,visited)
    if finish == 999:
        print(answer)
        break
    answer += 1