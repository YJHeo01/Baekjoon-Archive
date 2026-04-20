import math

n = int(input())

answer = int(math.log2(n))

if answer == 0: answer = 1

print(answer)