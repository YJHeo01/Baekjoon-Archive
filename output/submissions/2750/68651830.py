n = int(input())

num_list = []

for i in range(n):
    tmp = int(input())
    num_list.append(tmp)

num_list.sort()

for i in range(n):
    print(num_list[i])