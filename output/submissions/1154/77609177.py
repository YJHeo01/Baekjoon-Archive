import sys

input = sys.stdin.readline

n = int(input())

graph = [[]for _ in range(n+1)]
adj_matrix = [[False]*(n+1) for _ in range(n+1)]

while True:
    a,b = map(int,input().split())
    if a == -1:
        break
    adj_matrix[a][b] = True
    adj_matrix[b][a] = True

Team_B = []
adj_matrix[1][1] = True

for i in range(2,n+1):
    adj_matrix[i][i] = True
    if adj_matrix[1][i] == False:
        Team_B.append(i)

def check_correct_Team_A(adj_matrix,Team_B):
    for i in range(1,n+1):
        if i in Team_B:
            continue
        for j in range(1,n+1):
            if j in Team_B:
                continue
            if adj_matrix[i][j] == False:
                return False
    return True

def check_new_member_Team_B(adj_matrix,Team_B,new_member_idx):
    for i in Team_B:
        if adj_matrix[i][new_member_idx] == False:
            return False
    return True

def solution(adj_matrix,Team_B,new_member_idx):
    if check_correct_Team_A(adj_matrix,Team_B) == True:
        return Team_B
    ret_value = [-1]
    for i in range(new_member_idx+1,n+1):
        if i in Team_B:
            continue
        if check_new_member_Team_B(adj_matrix,Team_B,i) == False:
            continue
        ret_value = solution(adj_matrix,Team_B+[i],i)
        if ret_value[0] != -1:
            return ret_value
    return ret_value

Team_B = solution(adj_matrix,Team_B,1)

if Team_B == [] or Team_B[0] != -1:
    print(1)
    for i in range(1,n+1):
        if i not in Team_B:
            print(i,end=" ")
    print(-1)
    Team_B.sort()
    for i in Team_B:
        print(i,end=" ")
    print(-1)
else:
    print(-1)