#LGCPC 예선 제출 코드
#https://lgcpc.acmicpc.net/source/98206801

from collections import deque

p = int(input())

dp = [0] * (100*p+1)

INF = 998244353

dp[0] = 1

for i in range(p):
    n,m = map(int,input().split())
    subtask = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        graph[y].append(x)
    new_score = [0] * 101
    for bit_mask in range(1,1<<n):
        no = False
        for j in range(1,n+1):
            if (1 << (j-1)) & bit_mask == 0: continue
            for k in graph[j]:
                if bit_mask & (1<<(k-1)) == 0:
                    no = True
                    break
                queue = deque([k])
                visited = [False] * (n+1)
                visited[k] = True
                while queue:
                    x = queue.popleft()
                    for nx in graph[x]:
                        if visited[nx]: continue
                        if (1<<(nx-1)) & bit_mask == 0:
                            no = True
                            break
                        visited[nx] = True
                        queue.append(nx)
        if no: continue
        tmp = 0
        for k in range(n):
            if (1<<k) & bit_mask != 0:
                tmp += subtask[k+1]
        new_score[tmp] += 1
    for j in range(p*100,-1,-1):
        if dp[j] == 0: continue
        for k in range(101):
            dp[j+k] += dp[j] * new_score[k]
            dp[j+k] %= INF

answer = 0

for i in range(p*100+1):
    dp[i] %= INF
    answer += dp[i] * i
    answer %= INF
    
print(answer)