n = int(input())

num_list = []

for i in range(n):
    tmp = int(input())
    num_list.append(tmp)

for i in range(n,0,-1):
    for j in range(i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

for i in range(n):
    print(num_list[i])