INF = 100001
n = int(input())

arr = list(map(int,input().split()))

cut_line = sum(arr) // 2

party = []

for i in range(n):
    party.append((arr[i],i+1))
    
party.sort(reverse=True)

dp = [False] * INF
dp[0] = True
target = 0

for value,idx in party:
    for i in range(cut_line,-1,-1):
        if i + value >= INF: continue
        if dp[i] == True:
            dp[i+value] = True
            target = max(target,i + value)

answer = []

for value, idx in party:
    if value > target: continue
    if dp[target-value] == True:
        answer.append(idx)
        target -= value
    if target == 0: break

print(len(answer))
print(*sorted(answer))