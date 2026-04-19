import sys, heapq

input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]

q = []

parent = list(range(n))

for i in range(1,n):
    heapq.heappush(q,(max(array[i],array[i-1]),-min(array[i],array[i-1]),i-1,i))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(array,parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if array[a] < array[b]:
        parent[a] = b
    else:
        parent[b] = a

answer = 0

while q:
    max_value, min_value, l, r = heapq.heappop(q)
    if find_parent(parent,l) == find_parent(parent,r): continue
    min_value *= -1
    max_v, min_v = max(array[find_parent(parent,l)],array[find_parent(parent,r)]), min(array[find_parent(parent,l)],array[find_parent(parent,r)])
    #if max_v != max_value or min_v != min_v:
        #heapq.heappush(q,(max_v,-min_v,l,r))
        #continue
    answer += (max_value-min_value)
    union_parent(array,parent,l,r)
    left = l - 1
    while True:
        if left == -1: break
        if find_parent(parent,left) != find_parent(parent,l):
            left_v = array[find_parent(parent,left)]
            new_max, new_min = max(left_v,max_v), min(left_v,max_v)
            heapq.heappush(q,(new_max,-new_min,left,l))
            break
        left -= 1
    right = r + 1
    while True:
        if right == n: break
        if find_parent(parent,right) != find_parent(parent,r):
            right_v = array[find_parent(parent,right)]
            new_max, new_min = max(right_v,max_v), min(right_v,max_v)
            heapq.heappush(q,(new_max,-new_min,r,right))
            break

print(answer)