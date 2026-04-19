import sys

input = sys.stdin.readline

n = int(input())

state = [0] * 200001

answer = 0

for _ in range(n):
    a,b = map(int,input().split())
    if b == 1:
        answer += state[a]
        state[a] = 1
    else:
        if state[a] == 0:
            answer += 1
        else:
            state[a] = 0
            
answer += sum(state)

print(answer)