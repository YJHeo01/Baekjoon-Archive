import sys

input = sys.stdin.readline

sys.setrecursionlimit(2*(10**5))

t = int(input())

def dfs(arr,check,cycle,finish,x):
    nx = arr[x]
    if check[nx] == True:
        cycle[nx] = True
        return
    if finish[nx]:
        check[x] = False
        return
    check[nx] = True
    dfs(arr,check,cycle,finish,nx)
    finish[x] = True
    check[nx] = False

def dfs_(arr,start,x):
    nx = arr[x]
    if nx == start: return 1
    return dfs_(arr,start,nx) + 1

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    check = [False] * (n+1)
    cycle = [False] * (n+1)
    finish = [False] * (n+1)
    for i in range(1,n+1):
        if finish[i]: continue
        check[i] = True
        dfs(arr,check,cycle,finish,i)
        check[i] = False
    answer = n
    for i in range(1,n+1):
        if cycle[i]:
            answer -= dfs_(arr,i,i)
    print(answer)