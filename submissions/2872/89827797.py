import sys

input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]

answer = 0

target = n

visited = [False] * (n+1)

while array:
    tmp = array.pop()
    visited[tmp] = True
    if tmp == target:
        while True:
            if visited[target] == False: break
            target -= 1
    else:
        answer = max(answer,tmp)
    
print(answer)