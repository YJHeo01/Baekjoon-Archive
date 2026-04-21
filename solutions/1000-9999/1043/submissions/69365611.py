from collections import deque

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

n,m = map(int,input().split())

human = deque(list(map(int,input().split())))

human.popleft()

def union_parent(parent,party):
    global human
    l = party[0] + 1
    for i in range(1,l):
        party[i] = find_parent(parent,party[i])
    for i in range(1,l):
        if party[i] in human:
            for j in range(1,l):
                parent[party[j]] = party[i]
            return
    parent_v = min(party[1:])
    for i in range(1,l):
        parent[party[i]] = parent_v
    return
            

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i
party_list = []
answer = 0

for _ in range(m):
    tmp = list(map(int,input().split()))
    union_parent(parent,tmp)
    party_list.append(tmp)

for party in party_list:
    answer += 1
    for i in range(1,party[0]+1):
        if find_parent(parent,party[i]) in human:
            answer -= 1
            break

print(answer)