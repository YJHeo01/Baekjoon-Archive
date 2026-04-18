from itertools import combinations

n,k = map(int,input().split())

test_case_list = list(combinations(range(n),k))

adj_matrix = [list(map(int,input().split())) for _ in range(n)]

answer = -int(1e9)

for test_case in test_case_list:
    tmp = 0
    for i in range(k):
        for j in range(i):
            tmp += adj_matrix[test_case[i]][test_case[j]]
    answer = max(answer,tmp)
    
print(answer)