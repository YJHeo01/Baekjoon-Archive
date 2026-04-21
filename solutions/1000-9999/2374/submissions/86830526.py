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
        array[b] = a

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
    if l != 0:
        left_v = array[find_parent(parent,l-1)]
        new_max, new_min = max(left_v,max_v), min(left_v,max_v)
        heapq.heappush(q,(new_max,-new_min,l-1,l))
    if r + 1 != n:
        right_v = array[find_parent(parent,r+1)]
        new_max, new_min = max(right_v,max_v), min(right_v,max_v)
        heapq.heappush(q,(new_max,-new_min,r,r+1))

print(answer)