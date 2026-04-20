n = int(input())

arr = list(map(int,input().split()))

sum_value = sum(arr)
max_value = max(arr)

if max_value * 2 <= sum_value:
    print("Happy")
else:
    print("Unhappy")