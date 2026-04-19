n,m = map(int,input().split())

array = [list(map(int,input().split()))for _ in range(n)]

answer = -1001

for _ in range(2):
    
    array.reverse()
    dp_A = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            dp_A[i+1][j+1] = array[i][j]
            if i != 0:
                dp_A[i+1][j+1] = max(dp_A[i+1][j+1],dp_A[i][j+1]+array[i][j])
            if j != 0:
                dp_A[i+1][j+1] = max(dp_A[i+1][j+1],dp_A[i+1][j]+array[i][j])
            answer = max(answer,dp_A[i+1][j+1])
        
print(answer)