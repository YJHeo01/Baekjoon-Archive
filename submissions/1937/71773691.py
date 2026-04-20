import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

forest = []

for _ in range(n):
    forest.append(list(map(int,input().split())))

def dfs(start,move_cnt):
    ret_value = move_cnt
    x,y = start[0], start[1]
    if x - 1 >= 0 and forest[x-1][y] > forest[x][y]:
        ret_value = max(ret_value,dfs((x-1,y),move_cnt+1))
    if y - 1 >= 0 and forest[x][y-1] > forest[x][y]:
        ret_value = max(ret_value,dfs((x,y-1),move_cnt+1))
    if x + 1 < n and forest[x+1][y] > forest[x][y]:
        ret_value = max(ret_value,dfs((x+1,y),move_cnt+1))
    if y + 1 < n and forest[x][y+1] > forest[x][y]:
        ret_value = max(ret_value,dfs((x,y+1),move_cnt+1))
    return ret_value

answer = 0

for i in range(n):
    for j in range(n):
        visited = [[False]*n for _ in range(n)]
        answer = max(answer,dfs((i,j),1))

print(answer)
