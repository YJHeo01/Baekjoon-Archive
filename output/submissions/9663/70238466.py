from itertools import permutations

n = int(input())

point_list = [0] * n

for i in range(n):
    point_list[i] = i

result = list(permutations(point_list,n))

def check_queen(queen_list):
    for i in range(n):
        for j in range(i):
            if abs(i-j) == abs(queen_list[i] - queen_list[j]) or queen_list[i] == queen_list[j]:
                return 0
            
    return 1

answer = 0
for list in result:
    answer += check_queen(list)

print(answer)
    