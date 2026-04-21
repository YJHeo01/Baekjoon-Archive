import sys

input = sys.stdin.readline

n = int(input())

stack = []

array = [int(input()) for _ in range(n)]

answer = 0

for i in range(n):
    answer = max(answer,array[i])
    if array[i] == 0:
        while stack:
            high, idx = stack.pop()
            answer = max(answer,(i-idx)*high)
        continue
    while stack:
        high, idx = stack.pop()
        if array[i] > high:
            answer = max(answer,(i-idx+1)*high)
            stack.append((high,idx))
            break
        else:
            answer = max(answer,(i-idx+1)*array[i])
    stack.append((array[i],i))
            
while stack:
    high,idx = stack.pop()
    answer = max(answer,high*(n-idx))

print(answer)