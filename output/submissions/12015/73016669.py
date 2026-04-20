n = int(input())

length_min_list = [0] * (n+1)

answer = 0

num_list = list(map(int,input().split()))

for i in range(n):
    if num_list[i] > length_min_list[answer]:
        answer += 1
        length_min_list[answer] = num_list[i]
        continue
    for j in range(answer,0,-1):
        if num_list[i] >= length_min_list[j]:
            break
        if num_list[i] > length_min_list[j-1]:
            length_min_list[j] = num_list[i]
print(answer)