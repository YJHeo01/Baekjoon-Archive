n = int(input())

num_list = [0] + list(map(int,input().split()))

answer = [11] * n
for i in range(1,n+1):
    idx = num_list[i]
    rank = 0
    while idx >= rank:
        if answer[rank] < i:
            idx += 1
        rank += 1
    answer[idx] = i

for i in answer:
    print(i,end=" ")