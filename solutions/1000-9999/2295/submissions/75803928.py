n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

answer = -1

for left in range(n-2):
    for right in range(left+2,n):
        for target_idx in range(n-1,answer,-1):
            target_value = array[target_idx]
            if array[right] + array[left] + array[left+1] > target_value:
                break
            target_value -= array[left]
            target_value -= array[right]
            left += 1
            right -= 1
            while left <= right:
                mid = (left+right) // 2
                if array[mid] > target_value:
                    right = mid - 1
                elif array[mid] < target_value:
                    left = mid + 1
                else:
                    answer = target_idx
                    break
    
print(array[answer])
