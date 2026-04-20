n = int(input())

num_list = []

answer = 0

for _ in range(n):
    num_list.append(int(input()))
    
for i in range(n-1,0,-1):
    if num_list[i] <= num_list[i-1]:
        answer += (num_list[i-1] - num_list[i] + 1)
        num_list[i-1] = num_list[i] - 1

print(answer)