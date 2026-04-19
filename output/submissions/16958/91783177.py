import sys

input = sys.stdin.readline

n,t = map(int,input().split())

city = []

special = [False] * n

for i in range(n):
    s,x,y = map(int,input().split())
    city.append((x,y))
    if s == 1: special[i] = True

nearest_special = list(range(n))

for i in range(n):
    if special[i]: continue
    x_i,y_i = city[i]
    for j in range(n):
        if special[j] == False: continue
        if nearest_special[i] == i:
            nearest_special[i] = j
            continue
        x_j, y_j = city[j]
        x_k, y_k = city[nearest_special[i]]
        if abs(x_i-x_j) + abs(y_i-y_j) < abs(x_k-x_i) + abs(y_i-y_k):
            nearest_special[i] = j

m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    a -= 1; b -= 1
    x_a, y_a = city[a]
    x_b, y_b = city[b]
    answer = abs(x_a-x_b) + abs(y_a-y_b)
    x_1, y_1 = city[nearest_special[a]]
    x_2, y_2 = city[nearest_special[b]]
    answer = min(answer,abs(x_1-x_a)+abs(y_1-y_a)+t+abs(x_2-x_b)+abs(y_2-y_b))
    print(answer)