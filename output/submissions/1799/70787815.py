from itertools import combinations

n = int(input())

board = []

void_point = []
max_value = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1:
            void_point.append((i,j))
            max_value += 1

case_list = list(combinations(void_point,n))


def check_case(positions):
    l = len(positions)
    for i in range(l-1):
        for j in range(i+1,l):
            if (positions[i][0] == positions[j][1] and positions[j][0] == positions[i][1]) or abs(positions[i][0]-positions[j][0]) == abs(positions[i][1]-positions[j][1]):
                return False
    return True
    
answer = 0
for i in range(max_value,0,-1):
    case_list = list(combinations(void_point,i))
    for case in case_list:
        if check_case(case) == True:
            answer = i
            break
    if answer != 0:
        break

print(answer)