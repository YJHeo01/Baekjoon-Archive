n = int(input())

arr = sorted(list(map(int,input().split())))

arr.reverse()

Alice = sum(arr[:n//2])

Bob = sum(arr[n//2:])

if Alice:
    print("Alice")
else:
    print("Bob")