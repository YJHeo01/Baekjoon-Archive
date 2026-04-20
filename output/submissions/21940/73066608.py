import sys

input = sys.stdin.readline

n,m = map(int,input().split())
INF = int(1e9)
adj_matrix = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,t = map(int,input().split())
    adj_matrix[a][b] = min(adj_matrix[a][b],t)

for i in range(1,n+1):
    adj_matrix[i][i] = 0
k = int(input())

city_list = list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(1,n+1):
        for x in range(1,n+1):
            adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][x]+adj_matrix[x][j])

min_distance = INF
answer = []
for middle_city in range(1,n+1):
    distance_sum = 0
    for city in city_list:
        distance_sum  = max(distance_sum,adj_matrix[city][middle_city]+adj_matrix[middle_city][city])
    if distance_sum < min_distance:
        min_distance = distance_sum
        answer = [middle_city]
    elif distance_sum == min_distance:
        answer.append(middle_city)
    else:
        continue

for city in answer:
    print(city,end=" ")