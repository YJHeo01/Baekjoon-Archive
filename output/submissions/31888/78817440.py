import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())

table = [[]]

for _ in range(n):
    table.append(list(map(int,input().split())))

def solution(table,visited,vx):
    if vx == e:
        return True
    ret_value = False
    guard = True
    for nx in table[vx]:
        if visited[nx] == True:continue
        if nx == e:
            if guard == True:
                guard = False
                continue
        visited[nx] = True
        ret_value = solution(table,visited,nx)
        visited[nx] = False
        if ret_value == True: break
    return ret_value
    
visited = [False] * (n+1)
for e in range(1,n+1):
    visited[1] = True
    yes = solution(table,visited,1)
    if yes == True:
        print("Yes")
    else:
        print("No")