#https://github.com/YJHeo01

import sys

input = sys.stdin.readline

g = int(input())

p = int(input())

gate = [False] * (g+1)

answer = 0
for i in range(p):
    airplane = int(input())
    docking = False
    for j in range(airplane,0,-1):
        if gate[j] == False:
            docking = True
            gate[j] = True
            answer += 1
            break
    if docking == False:
        break

print(answer)