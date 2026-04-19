import sys

input = sys.stdin.readline

n = int(input())

connected = [False] * (n+1)

for _ in range(n-2):
    a,b = map(int,input().split())
    connected[a] = True
    connected[b] = True

for i in range(1,n+1):
    if connected[i] == False:
        if i == n:
            print(i-1,i)
        else:
            print(i,i+1)
        break