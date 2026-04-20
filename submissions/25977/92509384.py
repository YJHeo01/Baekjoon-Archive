from collections import deque

n,k = map(int,input().split())

tree = [[] for _ in range(n)]

for _ in range(n-1):
    p,c = map(int,input().split())
    tree[p].append(c)
    tree[c].append(p)

arr = list(map(int,input().split()))

answer = 0

for bit_mask in range(1,1<<n):
    if bit_mask % 2 == 0: continue
    tmp = 1
    apple_cnt = 0
    pear_cnt = 0
    visited = [False] * n
    for j in range(n):
        if tmp & bit_mask != 0:
            visited[j] = True
            apple_cnt += arr[j] % 2
            pear_cnt += arr[j] // 2
        tmp <<= 1
    if apple_cnt > k: continue
    queue = deque([0])
    visited[0] = False
    while queue:
        x = queue.popleft()
        for nx in tree[x]:
            if visited[nx]:
                visited[nx] = False
                queue.append(nx)
    for i in range(n):
        if visited[i]: pear_cnt = 0
    answer = max(answer,pear_cnt)

print(answer)