n = int(input())

arr = list(map(int,input().split()))

arrA = []
arrB = []

for i in arr:
    if i % 2 == arr[0] % 2: arrA.append(i)
    else: arrB.append(i)
    
if len(arrA) != len(arrB):
    print(-1)
    exit(0)
    
answer = []

prime = [True] * 2001

prime[0] = False
prime[1] = False

for i in range(2,2001):
    if prime[i]:
        for j in range(i+i,2001,i):
            prime[j] = False

l = n // 2

adj = [[] for _ in range(l)]

for i in range(l):
    for j in range(l):
        if prime[arrA[i]+arrB[j]]:
            adj[i].append(j)

def dfs(A,B,visited,a):
    visited[a] = True
    for b in adj[a]:
        if B[b] == -1 or (visited[B[b]] == False and dfs(A,B,visited,B[b])):
            A[a] = b
            B[b] = a
            return 1
    return 0

for i in adj[0]:
    A = [-1] * l
    B = [-1] * l
    A[0] = i
    B[i] = 0
    tmp = l - 1
    for j in range(1,l):
        if A[j] != -1: continue
        visited = [False] * l
        visited[0] = True
        tmp -= dfs(A,B,visited,j)
    if tmp == 0:
        answer.append(arrB[i])
        
if answer == []:
    print(-1)
    exit(0)

answer.sort()

print(*answer)