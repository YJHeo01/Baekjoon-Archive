n = int(input())

arr = sorted([int(input())for _ in range(n)])

arr = arr[1::]

print(sum(arr))