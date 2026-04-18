import sys

input = sys.stdin.readline

m = int(input())

S = set()

for _ in range(m):
    tmp = input().split()
    if tmp[0] == "add":
        S.add(int(tmp[1]))
    elif tmp[0] == "remove":
        if int(tmp[1]) in S:
            S.remove(int(tmp[1]))
    elif tmp[0] == 'toggle':
        if int(tmp[1]) in S:
            S.remove(int(tmp[1]))
        else:
            S.add(int(tmp[1]))
    elif tmp[0] == 'check':
        if int(tmp[1]) in S:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'all':
        for i in range(1,21):
            S.add(i)
    else:
        S = set() 