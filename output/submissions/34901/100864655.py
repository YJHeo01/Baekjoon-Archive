import heapq, sys

input = sys.stdin.readline

n = int(input())

info = [list(map(int,input().split())) for _ in range(n)]

q = []

parent = list(range(n))

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

for i in range(n):
  for j in range(i):
    heapq.heappush(q,(abs(info[i][0]-info[j][0])+abs(info[i][1]-info[j][1])+info[i][2]+info[j][2],i,j))

answer = 0

connect = 0

while q:
  if connect == n-1: break
  value,i,j=heapq.heappop(q)
  if find_parent(parent,i) == find_parent(parent,j): continue
  answer += value
  union_parent(parent,i,j)
  connect+=1

for i in range(n):
  answer -= info[i][2]
  
for i in range(n):
  print(answer+info[i][2],end=" ")