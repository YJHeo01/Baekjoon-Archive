from itertools import permutations

n = int(input())

men = [input() for _ in range(n)]

women = [input() for _ in range(n)]

data = list(range(n))

answer = 0

for test_case in list(permutations(data,n)):
    tmp = 0
    for i in range(n):
        for j in range(4):
            if men[i][j] != women[test_case[i]][j]: tmp += 1
    answer = max(answer,tmp)
    
print(answer)