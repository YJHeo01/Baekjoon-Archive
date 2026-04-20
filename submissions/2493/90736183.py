n = int(input())

answer = [0] * n

arr = list(map(int,input().split()))

stack = []

for i in range(n-1,-1,-1):
    while stack:
        high, idx = stack.pop()
        if arr[i] < high:
            stack.append((high,idx))
            break
        answer[idx] = i + 1
    stack.append((arr[i],i))

print(*answer)