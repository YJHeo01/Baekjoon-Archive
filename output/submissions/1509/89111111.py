s = list(input())

length = len(s)

def check_pel(left,right):
    while left < right:
        if s[left] != s[right]: return False
        left += 1; right -= 1
    return True

graph = [[] for _ in range(length+1)]

for i in range(1,length):
    for j in range(i):
        if check_pel(j,i):
            graph[i+1].append(j+1)
                

dp = [0] * (length+1)

for i in range(1,length+1):
    dp[i] = dp[i-1] + 1
    for j in graph[i]:
        dp[i] = min(dp[i],dp[j-1]+1)

print(dp[length])