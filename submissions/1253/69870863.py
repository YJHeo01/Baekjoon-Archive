n = int(input())

num_list = list(map(int,input().split()))

num_list.sort()

answer = 0
for i in range(n):
    left = 0
    right = n-1
    while left < right:
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue
        tmp = num_list[left] + num_list[right]
        if tmp < num_list[i]:
            left += 1
        elif tmp > num_list[i]:
            right -= 1
        else:
            answer += 1
            break

print(answer)
