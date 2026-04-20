#https://github.com/YJHeo01

import sys
input = sys.stdin.readline
n = int(input())

dp1 = [0] * (n+1)
dp2 = [0] * (n+1)

town_information = [[0,0]]

for _ in range(n):
    town_information.append(list(map(int,input().split())))

for i in range(2,n+1):
    dp1[i] = dp1[i-1] + (town_information[i][0] - town_information[i-1][0]) * (town_information[i-1][1])

for i in range(n-1,0,-1):
    dp2[i] = dp2[i+1] + (town_information[i+1][0] - town_information[i][0]) * (town_information[i+1][1])

answer = 0
INF = int(1e9)
min_sum_distance = INF

for i in range(1,n+1):
    tmp = dp1[i] + dp2[i]
    if min_sum_distance > tmp:
        min_sum_distance = tmp
        answer = i

print(answer)