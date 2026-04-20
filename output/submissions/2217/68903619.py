import sys
input = sys.stdin.readline

n = int(input())
answer = 0
ropes = []
for i in range(n):
    tmp = int(input())
    ropes.append(tmp)
ropes.sort(reverse=True)
for i in range(1,n+1):
    tmp = ropes[i-1] * (i)
    if tmp > answer:
        answer = tmp
    else:
        break
print(answer)