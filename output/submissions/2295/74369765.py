import sys

input = sys.stdin.readline

n = int(input())

num_list = []

for _ in range(n):
    num_list.append(int(input()))

num_list.sort()

answer = 0
n -= 1
for i in range(n-2):
    for j in range(i+2,n):
        for k in range(i,j):
            sum_num = num_list[i] + num_list[j] + num_list[k]
            if sum_num  > num_list[-1]:
                break
            left, right = j,n
            while left <= right:
                mid = (left+right) // 2
                if sum_num > num_list[mid]:
                    left = mid + 1
                elif sum_num < num_list[mid]:
                    right = mid - 1
                else:
                    answer = max(sum_num,answer)
                  

print(answer)