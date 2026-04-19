import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

adj_matrix = [[False]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    adj_matrix[i][i] = True

first_idx_friend = []

while True:
    a,b = map(int,input().split())
    if a == -1:
        break
    if a == 1:
        first_idx_friend.append(b)
    elif b == 1:
        first_idx_friend.append(a)
    else:
        adj_matrix[a][b] = True
        adj_matrix[b][a] = True

Team_A = [False] * (n+1)
Team_A[1] = True

def check_correct_Team_A(adj_matrix,Team_A):
    Team_member = []
    for i in range(2,n+1):
        if Team_A[i] == True:
            Team_member.append(i)
    length = len(Team_member)
    for i in range(length):
        for j in range(i+1,length):
            a,b = Team_member[i], Team_member[j]
            if adj_matrix[a][b] == False:
                return False
    return True

def check_complete_Team_B(adj_matrix,Team_A):
    Team_B = []
    for i in range(2,n+1):
        if Team_A[i] == False:
            Team_B.append(i)
    length = len(Team_B)
    for i in range(length):
        for j in range(i+1,length):
            a = Team_B[i]; b = Team_B[j]
            if adj_matrix[a][b] == False:
                return False
    return True

def dfs(first_idx_friend,adj_matrix,Team_A):
    if check_complete_Team_B(adj_matrix,Team_A) == True:
        return 1
    ret_value = -1
    length = len(first_idx_friend)
    for idx in range(length):
        Team_A[first_idx_friend[idx]] = True
        Team_A[first_idx_friend[idx]] = check_correct_Team_A(adj_matrix,Team_A)
        if Team_A[first_idx_friend[idx]] == False:
            continue
        ret_value = dfs(first_idx_friend[idx+1:],adj_matrix,Team_A)
        if ret_value == 1:
            break
        Team_A[first_idx_friend[idx]] = False
    return ret_value

answer = dfs(first_idx_friend,adj_matrix,Team_A)

print(answer)
if answer == 1:
    Team_B = []
    for i in range(1,n+1):
        if Team_A[i] == True:
            print(i,end=" ")
        else:
            Team_B.append(i)
    print(-1)
    for i in Team_B:
        print(i,end=" ")
    print(-1)