import sys
input = sys.stdin.readline

N, X, K = map(int,input().split())

game = [0]*(N+1)

game[X] = 1

for i in range(K):
    a,b = map(int,input().split())
    game[a], game[b] = game[b], game[a]

for i in range(1,N+1):
    if game[i] == 1:
        print(i)