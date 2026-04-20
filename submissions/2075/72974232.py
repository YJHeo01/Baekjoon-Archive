import sys

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int,input().split())))

first,second,third,fourth,fifth = n-1,n-1,n-1,n-1,n-1

for i in range(n):
    biggest_value = max(array[first][0],array[second][1],array[third][2],array[fourth][3],array[fifth][4])
    if biggest_value == array[first][0]:
        first -= 1
    elif biggest_value == array[second][1]:
        second -= 1
    elif biggest_value == array[third][2]:
        third -= 1
    elif biggest_value == array[fourth][3]:
        fourth -= 1
    else:
        fifth -= 1
    if i == n-1:
        print(biggest_value)
