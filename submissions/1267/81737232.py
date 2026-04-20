n = int(input())

array = list(map(int,input().split()))

cost_Y = 0
cost_M = 0

for i in range(n):
    cost_Y += (1 + array[i] // 30) * 10
    cost_M += (1 + array[i] // 60) * 15

if cost_Y > cost_M:
    print("M " + str(cost_M))
elif cost_Y < cost_M:
    print("Y "+str(cost_Y))
else:
    print("Y M "+str(cost_Y))