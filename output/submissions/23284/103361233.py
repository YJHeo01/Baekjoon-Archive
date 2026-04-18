from itertools import permutations

n = int(input())

data = list(range(1,n+1))

answer = list(permutations(data,n))

for row in answer:
    print(*row)