import sys

input = sys.stdin.readline

n = int(input())

stack = []

array = [int(input()) for _ in range(n)]

answer = 0

for i in range(n):
    answer = max(answer,array[i])
    while stack:
        high, idx = stack.pop()
        if array[i] > high:
            answer = max(answer,(i-idx+1)*high)
            stack.append((high,idx))
            break
        answer = max(answer,(i-idx+1)*array[i])
    stack.append((array[i],i))
            
while stack:
    high,idx = stack.pop()
    if high == 0: break
    answer = max(answer,high*(n-idx))

print(answer)