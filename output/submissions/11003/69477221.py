from collections import deque

n, l = map(int,input().split())

num_list = list(map(int,input().split()))

d = num_list[0]
D_list = deque([])
for i in range(l):
    D_list.append(num_list[i])
    if d > num_list[i]:
        d = num_list[i]
    print(d,end=" ")

for i in range(l,n):
    if d > num_list[i]:
        D_list.popleft()
        d = num_list[i]
        D_list.append(num_list[i])
    elif D_list[0] == d:
        D_list.popleft()
        D_list.append(num_list[i])
        d = min(D_list)
    else:
        D_list.popleft()
        D_list.append(num_list[i])
    print(d,end=" ")
