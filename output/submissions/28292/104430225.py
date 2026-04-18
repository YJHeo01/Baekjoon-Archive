import math

n = int(input())

answer = int(math.log2(n))

if answer == 0: answer = 1
if answer > 3: answer = 3

print(answer)