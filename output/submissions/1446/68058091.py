n, d = map(int,input().split())
road = [0]*(d+1)

start = [0]*n
end = [0]*n
distance = [0]*n

for i in range(n):
    start[i], end[i], distance[i] = map(int,input().split())
road[0] = 0
for i in range(1,d+1):
    road[i] = road[i-1] + 1
    if i in end:
        for j in range(n):
            if end[j] == i:
                road[i] = min(road[i],road[start[j]]+distance[j])

print(road[-1])