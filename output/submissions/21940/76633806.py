import sys

input = sys.stdin.readline

n,m = map(int,input().split())

INF = int(1e9)

time = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,t = map(int,input().split())
    time[a][b] = t

for i in range(n+1):
    time[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            time[i][j] = min(time[i][j],time[i][k]+time[k][j])

k = int(input())

city_list = list(map(int,input().split()))

answer_time = INF
answer_city = []

for i in range(1,n+1):
    tmp = 0
    for city in city_list:
        tmp = max(tmp,time[i][city]+time[city][i])
    if tmp < answer_time:
        answer_time = tmp
        answer_city = [i]
    elif tmp == answer_time:
        answer_city.append(i)
    else:
        continue

answer_city.sort()

for city in answer_city:
    print(city,end=" ")