import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))

pos = [0] * (n+1)

for i in range(n): pos[array[i]] = i

m = int(input())

for _ in range(m):
    l,r = map(int,input().split())
    new_pos = pos[:l] + sorted(pos[l:r+1]) + pos[r+1:]
    for i in range(1,n+1): array[new_pos[i]] = i
    print(*array)