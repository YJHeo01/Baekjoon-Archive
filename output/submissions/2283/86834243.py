import sys

input = sys.stdin.readline

INF = 1000001

n,k = map(int,input().split())
start = [0] * INF
end = [0] * INF

for _ in range(n):
    l,r = map(int,input().split())
    start[l] += 1; end[r] += 1

prefix_sum = [0] * INF

plus = 0

for i in range(INF):
    if i != 0:
        prefix_sum[i] = prefix_sum[i-1] + plus
    plus += start[i]
    plus -= end[i]

for a in range(INF):
    left, right = a, INF-1
    b = a
    while left <= right:
        mid = (left + right) // 2
        if prefix_sum[mid] - prefix_sum[a] >= k:
            b = mid
            right = mid - 1
        else:
            left = mid + 1
    if prefix_sum[b] - prefix_sum[a] == k:
        print(a,b)
        exit(0)

print(0,0)
