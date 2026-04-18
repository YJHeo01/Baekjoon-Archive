import math, sys

input = sys.stdin.readline

n = int(input())

town = []

for _ in range(n):
    town.append(list(map(int,input().split())))

answer = math.sqrt((town[n-1][0]-town[0][0])**2+(town[n-1][1]-town[0][1])**2)

print(answer)