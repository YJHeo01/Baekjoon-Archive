import sys

input = sys.stdin.readline

n,c = map(int,input().split())

arr = [0] + list(map(int,input().split()))

m = int(input())

answer = [0] * m

query = []

for idx in range(m):
    i,j = map(int,input().split())
    query.append((i,j,idx))

query.sort(key=lambda x:(x[1]-x[0],x[1],-x[0]))

visited = [False] * m

for i in range(m):
    if visited[i] == True: continue
    state = [0] * (c+1)
    max_color = 0
    left, right, idx = query[i]
    for x in range(left,right+1):
        color = arr[x]
        state[color] += 1
        if state[color] > state[max_color]: max_color = color
    if state[max_color] * 2 > (right-left+1): answer[idx] = max_color
    for j in range(i+1,m):
        l,r,idx = query[j]
        if visited[j] or r < right or l > left: continue
        visited[j] = True
        for x in range(l,left):
            color = arr[x]
            state[color] += 1
            if state[color] > state[max_color]: max_color = color
        for x in range(right+1,r+1):
            color = arr[x]
            state[color] += 1
            if state[color] > state[max_color]: max_color = color
        if state[max_color]*2 > (r-l+1): answer[idx] = max_color
        left = min(left,l)
        right = max(right,r)

for i in answer:
    if i == 0:
        print("no")
    else:
        print("yes"+" "+str(i))