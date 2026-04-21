n = int(input())

arr = sorted(list(map(int,input().split())))

left, right = 0,n-1

Alice = 0

Bob = 0

while left <= right:
    Bob += arr[left]
    if left == right: break
    Alice += arr[right]
    left += 1
    right -= 1

if Alice <= Bob or n % 2 == 1:
    print("Bob")
else:
    print("Alice")