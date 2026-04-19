def convert_value(value):
    if value.isupper() == True:
        return ord(value) - ord('A') + 27
    else:
        return ord(value) - ord('a') + 1

n = int(input())

parent = [0] * n

for i in range(1,n):
    parent[i] = i

_array = []

for i in range(n):
    _array.append(list(input()))

answer = 0

lan_cable_list = []
for i in range(n):
    for j in range(n):
        if _array[i][j] == '0':
            continue
        elif i != j:
            length = convert_value(_array[i][j])
            lan_cable_list.append((length,i,j))
        else:
            length = convert_value(_array[i][j])
            answer += length

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

lan_cable_list.sort()

for lan_cable in lan_cable_list:
    length, a, b = lan_cable
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
    else:
        answer += length

for i in range(n):
    if find_parent(parent,i) != 0:
        answer = -1
        break

print(answer)
