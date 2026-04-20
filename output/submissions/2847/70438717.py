n = int(input())

num_list = []

answer = 0

for i in range(n):
    num_list.append(int(input()))
    answer += i


for i in range(n-1):
    answer += (num_list[i] - num_list[n-1])
    
print(answer)