n = int(input())

array = list(map(int,input().split()))

sum_value = sum(array)

cutline = sum_value // 2 + sum_value % 2

max_value = max(array)

order = []

for i in range(n):
    order.append((array[i],i+1))

order.sort(reverse=True)

dp = [False] * (sum_value+1)

dp[0] = True

for i in array:
    for j in range(sum_value,-1,-1):
        if j - i < 0: break
        if dp[j-i]: dp[j] = True

def solution(target):
    min_value = target - cutline
    answer = []
    for value, idx in order:
        if value < min_value: break
        if target - value < 0: continue
        if dp[target-value]:
            answer.append(idx)
            target -= value
    if target == 0:
        print(len(answer))
        print(*sorted(answer))
        exit(0)
    
for i in range(max_value-1,-1,-1):
    if dp[cutline+i]:
        solution(cutline+i)
        
print(0)