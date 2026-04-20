import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

NGE_list = [-1] * n

max_v = 0

for i in range(n-1,-1,-1):
    if num_list[i] >= max_v:
        max_v = num_list[i]
    else:
        if num_list[i] < num_list[i+1]:
            NGE_list[i] = num_list[i+1]
            continue
        for j in range(i,n-1):
            if NGE_list[j] > num_list[i]:
                NGE_list[i] = NGE_list[j]
                break

for i in NGE_list:
    print(i,end=" ")
