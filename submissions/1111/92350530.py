n = int(input())
arr = list(map(int,input().split()))

if n == 1:
    print('A')
elif n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print('A')
else:
    a = (arr[2] - arr[1]) // (arr[1] - arr[0]) if arr[1] != arr[0] else 0
    b = arr[1] - arr[0] * a
    answer = arr[n-1] * a + b
    for i in range(1,n):
        if arr[i] != arr[i-1] * a + b:
            answer = 'B'
            break
    print(answer)