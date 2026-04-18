a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())

a = (c-a1)

answer = 1

if a * n0 < a0: answer = 0
if a < 0: answer = 0

print(answer)