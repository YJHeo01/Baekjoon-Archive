import sys

input = sys.stdin.readline

S = input().rstrip()

target = dict()

for c in S:
    if c in target:
        target[c] += 1
    else:
        target[c] = 1

n = int(input())

for _ in range(n):
    tmp = input().rstrip()
    password = dict()
    for c in tmp:
        if c in password:
            password[c] += 1
        else:
            password[c] = 1
    value = 1
    for c in target:
        if c not in password:
            password[c] = 0
        if target[c] > password[c]:
            value -= (target[c]-password[c])
    if value >= 0 and len(S) < len(tmp):
        print("YES")
    elif value == 0 and len(S) == len(tmp):
        print("YES")
    else:
        print("NO")
