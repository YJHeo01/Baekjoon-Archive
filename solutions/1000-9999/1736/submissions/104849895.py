n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

row_cnt = [0] * n
column_cnt = [0] * m

for i in range(n):
    for j in range(m):
        row_cnt[i] += grid[i][j]
        column_cnt[j] += grid[i][j]
        
answer = 0

for i in range(n):
    if row_cnt[i] == 0: continue
    answer += 1
    first_col = 0
    for j in range(m):
        if grid[i][j] == 1:
            first_col = j
        row_cnt[i] -= grid[i][j]
        column_cnt[j] -= grid[i][j]
    target = m-1
    while True:
        if target == first_col: break
        if column_cnt[target] != 0: break
        target -= 1
    for j in range(n):
        grid[j][target] -= 1
        row_cnt[j] -= 1
        column_cnt[target] -= 1

print(answer)