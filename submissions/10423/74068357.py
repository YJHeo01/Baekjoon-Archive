import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

power_plant_list = list(map(int,input().split()))

cable_list = []

for _ in range(m):
    u,v,w = map(int,input().split())
    cable_list.append((w,u,v))

city_plant = [0] * (n+1)

for i in range(1,n+1):
    city_plant[i] = i

cable_list.sort()

def find_plant(parent,x):
    if parent[x] != x:
        parent[x] = find_plant(parent,parent[x])
    return parent[x]

def union_plant(parent,a,b):
    a = find_plant(parent,a)
    b = find_plant(parent,b)
    if a in power_plant_list:
        parent[b] = a
    elif b in power_plant_list:
        parent[a] = b
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0

for w,u,v in cable_list:
    u_plant = find_plant(city_plant,u)
    v_plant = find_plant(city_plant,v)
    if u_plant == v_plant or ((u_plant in power_plant_list) and (v_plant in power_plant_list)):
        continue
    union_plant(city_plant,u,v)
    answer += w

print(answer)