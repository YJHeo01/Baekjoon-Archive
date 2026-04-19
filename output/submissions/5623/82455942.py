import sys

input = sys.stdin.readline

n = int(input())

if n == 2:
    print("1 1")
    exit(0)

matrix = [list(map(int,input().split())) for _ in range(n)]

a = [0] * n

a[1] = (matrix[0][1] + matrix[1][2] - matrix[0][2]) // 2
a[0] = matrix[0][1] - a[1]

for i in range(2,n):
    a[i] = matrix[i][i-1] - a[i-1]

print(*a)