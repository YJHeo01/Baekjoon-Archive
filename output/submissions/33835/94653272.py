import math

n = int(input())

town = []

for _ in range(n):
    town.append(list(map(int,input().split())))

answer = 0

for i in range(1,n):
    answer += math.sqrt((town[i][0]-town[i-1][0])**2+(town[i][1]-town[i-1][1])**2)

print(answer)