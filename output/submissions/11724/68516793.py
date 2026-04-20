import sys
input = sys.stdin.readline

n,m = map(int,input().split())

vertex = [0]*(n+1)
not_edge = [1]*(n+1)
edge = []
for i in range(m):
    a,b = map(int,input().split())
    if a > b: 
        a,b= b,a
    edge.append((a,b))
    not_edge[a]=0
    not_edge[b]=0
cnt = 0
for i in range(1,n+1):
    if not_edge[i] == 1:
        cnt += 1
edge.sort()

for e in edge:
    if vertex[e[0]] == 0:
        vertex[e[0]] = e[0]
    vertex[e[1]] = vertex[e[0]]

v_list = []
for i in range(1,n+1):
    if vertex[i] not in v_list:
        v_list.append(vertex[i])
print(len(v_list)+cnt)