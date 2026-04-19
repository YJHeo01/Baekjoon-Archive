n,m = map(int,input().split())

array = list(map(int,input().split()))

array.sort()

left, right = 0,n-1

plus_start_idx = 0

while left <= right:
    mid = (left + right) // 2
    if array[mid] >= 0:
        plus_start_idx = mid
        right = mid - 1
    else:
        left = mid + 1

answer = 0

no_return_value = 0
for i in range(0,plus_start_idx,m):
    answer -= 2 * array[i]

for i in range(n-1,plus_start_idx-1,-m):
    answer += 2 * array[i]

answer -= max(array[n-1],-array[0])
print(answer)