import sys

input = sys.stdin.readline

m = int(input())

arr = [0] * 21

for _ in range(m):
    tmp = input().split()
    if tmp[0] == "add":
        arr[int(tmp[1])] = 1
    elif tmp[0] == "remove":
        arr[int(tmp[1])] = 0
    elif tmp[0] == 'toggle':
        if arr[int(tmp[1])] == 0:
            arr[int(tmp[1])] = 1
        else:
            arr[int(tmp[1])] = 0
    elif tmp[0] == 'check':
        print(arr[int(tmp[1])])
    elif tmp[0] == 'all':
        for i in range(1,21):
            arr[i] = 1
    else:
        for i in range(21):
            arr[i] = 0