from itertools import permutations

n = int(input())

data = list(range(1,n+1))

answer = list(permutations(data,n))

for row in answer:
    not_answer = False
    for i in range(1,n-1):
        if row[i] < row[i-1] and row[i] < row[i+1] and row[i-1] > row[i+1]: not_answer = True
    if not_answer: continue
    print(*row)