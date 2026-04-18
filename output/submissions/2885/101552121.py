import math

k = int(input())

size = 1<<int(math.log2(k)+1)

cnt = 0

bit = 0

while True:
    if 1 << bit > k: break
    if (1 << bit) & k: cnt += 1
    bit += 1

print(size,cnt)