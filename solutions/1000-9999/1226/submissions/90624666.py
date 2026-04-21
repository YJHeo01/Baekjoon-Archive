INF = 100001
n = int(input())

arr = list(map(int,input().split()))

cut_line = sum(arr) // 2 + sum(arr) % 2

party = []

for i in range(n):
    party.append((arr[i],i+1))
    
party.sort(reverse=True)

dp = [[] for _ in range(INF)]

for value,idx in party:
    for i in range(cut_line,0,-1):
        if i + value >= INF: continue
        if dp[i] != []:
            dp[i+value] = dp[i] + [idx]
    dp[value] = [idx]
    
while dp:
    tmp = dp.pop()
    if tmp == []: continue
    print(len(tmp))
    print(*sorted(tmp))
    break