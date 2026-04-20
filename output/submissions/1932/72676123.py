#https://github.com/YJHeo01/BOJ
import sys

input = sys.stdin.readline

n = int(input())


tri = []
tri.append([int(input())])
for i in range(1,n):
    tri.append(list(map(int,input().split())))
    tri[i][0] += tri[i-1][0]
    tri[i][i] += tri[i-1][i-1]
    for j in range(1,i):
        tri[i][j] += max(tri[i-1][j-1],tri[i-1][j])

print(max(tri[n-1]))      
