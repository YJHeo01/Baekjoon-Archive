import math

n = int(input())

answer = math.comb(n,2)

if n == 3: answer = 1

print(answer)