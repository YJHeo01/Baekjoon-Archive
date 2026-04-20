import sys

input = sys.stdin.readline

g = int(input())
p = int(input())

docking_start_gate = [0] * (g+1)
gate = [False] * (g+1)
for i in range(1,g+1):
    docking_start_gate[i] = i
answer = 0

for _ in range(p):
    airplane = int(input())
    for i in range(docking_start_gate[airplane],-1,-1):
        if gate[i] == False:
            gate[i] = True
            answer += 1
            docking_start_gate[airplane] = i-1
            break
    if gate[0] == True:
        answer -= 1
        break
    

print(answer)