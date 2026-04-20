import sys

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int,input().split())))

idx_list = [n-1] * (5)

for _ in range(n-1):
    biggest_value = max(array[0][idx_list[0]],array[1][idx_list[1]],array[2][idx_list[2]],array[3][idx_list[3]],array[4][idx_list[4]])
    if biggest_value == array[0][idx_list[0]]:
        idx_list[0] -= 1
    elif biggest_value == array[1][idx_list[1]]:
        idx_list[1] -= 1
    elif biggest_value == array[2][idx_list[2]]:
        idx_list[2] -= 1
    elif biggest_value == array[3][idx_list[3]]:
        idx_list[3] -= 1
    else:
        idx_list[4] -= 1

answer = max(array[0][idx_list[0]],array[1][idx_list[1]],array[2][idx_list[2]],array[3][idx_list[3]],array[4][idx_list[4]])

print(answer)