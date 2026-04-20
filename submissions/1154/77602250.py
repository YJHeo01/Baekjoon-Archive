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

def check_complete_Team_B(adj_matrix,Team_A):
    A = []
    Team_B = []
    for i in range(1,n+1):
        if Team_A[i] == False:
            Team_B.append(i)
        else:
            A.append(i)
    for i in A:
        if i == 1:
            continue
        for j in A:
            if j == 1:
                continue
            if adj_matrix[i][j] == False:
                return False

    for i in Team_B:
        for j in Team_B:
            if adj_matrix[i][j] == False:
                return False
    return True

def dfs(first_idx_friend,adj_matrix,Team_A):
    if check_complete_Team_B(adj_matrix,Team_A) == True:
        return 1
    ret_value = -1
    for idx in first_idx_friend:
        if Team_A[idx] == True:
            continue
        Team_A[idx] = True
        ret_value = dfs(first_idx_friend,adj_matrix,Team_A)
        if ret_value == 1:
            break
        Team_A[idx] = False
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