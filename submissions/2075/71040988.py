n = int(input())
idx_list = [n-1] * n
num_list = []
for _ in range(n):
    num_list.append(list(map(int,input().split())))

for _ in range(n):
    biggest_line = 0
    biggest_value = 0
    for i in range(n):
        if num_list[i][idx_list[i]] > biggest_value:
            biggest_value = num_list[i][idx_list[i]]
            biggest_line = i
    idx_list[biggest_line] -= 1

print(biggest_value)