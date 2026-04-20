import sys

input = sys.stdin.readline

S = [set() for _ in range(501)]

n,m = map(int,input().split())

for _ in range(n):
    tmp = input().rstrip()
    length = len(tmp)
    for i in range(length):
        S[i+1].add(tmp[:i+1])

answer = 0

for _ in range(m):
    tmp = input().rstrip()
    length = len(tmp)
    for i in range(length):
        if tmp[:i+1] in S[i+1]:
            answer += 1
            break
        
print(answer)