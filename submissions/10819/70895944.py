from itertools import permutations

n = int(input())

idx_list = [0] * n

for i in range(1,n):
    idx_list[i] = i

test_case_list = list(permutations(idx_list,n))
array = list(map(int,input().split()))

answer = 0
for test_case in test_case_list:
    tmp = 0
    for i in range(n-1):
        tmp += abs(array[test_case[i]] -array[test_case[i+1]])
    answer = max(answer,tmp)

print(answer) 