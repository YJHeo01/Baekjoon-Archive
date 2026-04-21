n = int(input())

array = list(map(int,input().split()))

stack = []

answer = [-1] * n

for i in range(n-1,-1,-1):
    while stack:
        tmp = stack.pop()
        if array[i] < tmp:
            stack.append(tmp)
            answer[i] = tmp
            break
    stack.append(array[i])
    
print(*answer)