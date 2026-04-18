n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))
    
for _ in range(5000000):
    arr.sort()
    if arr[0][0] == arr[n-1][0]: break
    arr[0][0] += ((arr[n-1][0]-arr[0][0]) // arr[0][1]) * arr[0][1]
    if arr[0][0] < arr[n-1][0]: arr[0][0] += arr[0][1]

if arr[0][0] == arr[n-1][0]:
    print(arr[0][0])
else:
    print(-1)