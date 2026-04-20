n = int(input())

tri = [] * n
for i in range(n):
    tri.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        tmp_1 = 0
        tmp_2 = 0
        if j - 1 >= 0:
            tmp_1 = tri[i-1][j-1] + tri[i][j]
        if j <= i-1:
            tmp_2 = tri[i-1][j] + tri[i][j]
        tri[i][j] = max(tmp_1,tmp_2)

print(max(tri[n-1]))        
