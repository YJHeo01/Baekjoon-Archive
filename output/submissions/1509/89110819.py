s = list(input())

length = len(s)

table = dict()

for i in range(length):
    c = s[i]
    if c in table:
        table[c].append(i)
    else:
        table[c] = [i]

def check_pel(left,right):
    while left < right:
        if s[left] != s[right]: return False
        left += 1; right -= 1
    return True

graph = [[] for _ in range(length+1)]
for alphabet in table:
    cnt = len(table[alphabet])
    for i in range(1,cnt):
        for j in range(i):
            start, end = table[alphabet][j], table[alphabet][i]
            if check_pel(start,end):
                graph[end+1].append(start+1)
                

dp = [0] * (length+1)

for i in range(1,length+1):
    dp[i] = dp[i-1] + 1
    for j in graph[i]:
        dp[i] = min(dp[i],dp[j-1]+1)

print(dp[length])