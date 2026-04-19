import math

n = int(input())

answer = 0

tmp = 1

INF = 1000000007

for k in range(1,n+1):
    tmp <<= 1
    if tmp > INF: break
    answer += math.comb(n,k) * tmp

print(answer)