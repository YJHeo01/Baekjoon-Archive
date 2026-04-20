import sys

input = sys.stdin.readline

alpha = dict()

q = int(input())

answer = 0
for _ in range(q):
    c, name, *tmp = input().split()
    if c == '1':
        if name in alpha:
            alpha[name] += list(map(int,tmp[1:]))
        else:
            alpha[name] = list(map(int,tmp[1:]))
    else:
        if name not in alpha: continue
        alpha[name].sort()
        for _ in range(int(tmp[0])):
            if alpha[name] == []: break
            answer += alpha[name].pop()
            
print(answer)