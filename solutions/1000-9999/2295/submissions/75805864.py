n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

answer = 3

for target_idx in range(n-1,3,-1):
    for right in range(2,target_idx):
        for left in range(right-1):
            tmp_left = left; tmp_right = right
            if array[left] + array[right] + array[left+1] > array[target_idx]:
                break
            target_value = array[target_idx]
            target_value -= array[left]
            target_value -= array[right]
            tmp_left += 1
            tmp_right -= 1
            while tmp_left <= tmp_right:
                mid = (tmp_left+tmp_right) // 2
                if array[mid] > target_value:
                    tmp_right = mid - 1
                elif array[mid] < target_value:
                    tmp_left = mid + 1
                else:
                    answer = target_idx
                    break
    if answer > 3:
        break



print(array[answer])