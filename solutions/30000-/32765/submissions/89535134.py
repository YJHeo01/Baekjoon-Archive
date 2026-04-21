import sys

input = sys.stdin.readline

x,q = map(int,input().split())

INF = 10000

array = [x]

last_value = x

for i in range(1,INF+1):
    last_value = (last_value // i) * i + i
    array.append(last_value)

for _ in range(q):
    a = int(input())
    if a < INF:
        print(array[a])
    else:
        print(array[INF]+(a-INF)*(array[INF]-array[INF-1]))