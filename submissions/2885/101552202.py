import math

k = int(input())

size = 1<<int(math.log2(k))

if size < k: size *= 2

tmp = 0

cnt = 0

bit = size

while bit:
    if bit & k: cnt = tmp
    tmp += 1
    bit //= 2
    
print(size,cnt)