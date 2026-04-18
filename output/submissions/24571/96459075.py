import sys

input = sys.stdin.readline

friend = dict()

enemy = dict()

X = int(input())

for i in range(X):
    a,b = input().rstrip().split()
    if a in friend:
        friend[a].append((b,i))
    else:
        friend[a] = [(b,i)]
    if b in friend:
        friend[b].append((a,i))
    else:
        friend[b] = [(a,i)]

Y = int(input())

for i in range(Y):
    a,b = input().rstrip().split()
    if a in enemy:
        enemy[a].append((b,i))
    else:
        enemy[a] = [(b,i)]
    if b in enemy:
        enemy[b].append((a,i))
    else:
        enemy[b] = [(a,i)]

warning = [False] * (X+Y)

G = int(input())

for _ in range(G):
    names = list(input().rstrip().split())
    for i in range(3):
        if names[i] in friend:
            for target, idx in friend[names[i]]:
                if target not in names:
                    warning[idx] = True
        if names[i] in enemy:
            for target, idx in enemy[names[i]]:
                if target in names:
                    warning[idx+X] = True

answer = sum(warning)

print(answer)