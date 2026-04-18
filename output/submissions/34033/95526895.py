import sys

input = sys.stdin.readline

n,m = map(int,input().split())

D = dict()

for _ in range(n):
    a,b = input().split()
    D[a] = int(b)
    
answer = 0

for _ in range(m):
    c,d = input().split()
    if int(d) * 100 > 105 * D[c]: answer += 1
    
print(answer)