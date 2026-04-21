import sys

input = sys.stdin.readline

def Euclidean(a,b):
    if b == 0:
        return a
    return Euclidean(b,a%b)

n = int(input())

tree = [int(input()) for _ in range(n)]

distance = tree[1] - tree[0]

for i in range(2,n):
    distance = Euclidean(max(distance,tree[i]-tree[i-1]),min(distance,tree[i]-tree[i-1]))

answer = 0

for i in range(1,n):
    answer += (tree[i] - tree[i-1] - distance) // distance

print(answer)