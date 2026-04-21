from itertools import combinations
from collections import deque

n, m = map(int,input().split())

city = []

chicken = []
house_list = []
house_cnt = 0
for i in range(n):
    city_row = list(map(int,input().split()))
    for j in range(n):
        if city_row[j] == 2:
            chicken.append((i,j))
        elif city_row[j] == 1:
            house_list.append((i,j))
            house_cnt += 1
    city.append(city_row)

test_case_list = list(combinations(chicken,m))
INF = int(1e9)


answer = INF

for test_case in test_case_list:
    house_distance = [INF] * house_cnt
    for case in test_case:
        for i in range(house_cnt):
            house_distance[i] = min(house_distance[i],abs(house_list[i][0]-case[0]) + abs(house_list[i][1]-case[1]))
    answer = min(answer,sum(house_distance))

    print(answer)
