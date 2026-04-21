from itertools import permutations

INF = int(1e9)
n = int(input())
W = [list(map(int,input().split())) for _ in range(n)]
test_cast_list = list(permutations(list(range(n)),n))
answer = INF

for test_case in test_cast_list:
    tmp = 0
    for k in range(n):
        i,j = test_case[(k-1)%n], test_case[k]
        if W[i][j] != 0:
            tmp += W[i][j]
        else:
            tmp += INF
            break
    answer = min(answer,tmp)

print(answer)