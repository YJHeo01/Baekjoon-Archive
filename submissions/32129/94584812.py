import sys

input = sys.stdin.readline

n,q = map(int,input().split())

worth = list(map(int,input().split()))

answer = worth[0]

cnt = worth[0]

need = 0

idx = 0

for _ in range(q):
    command = list(map(int,input().split()))
    if command[0] == 1:
        x = command[1]
        cnt += x
        if cnt >= answer * (idx+1):
            tmp = cnt // (idx+1)
            if idx != n-1:
                if tmp >= worth[idx+1]:
                    if cnt % (idx+1) != 0: tmp += 1
                    cnt += worth[idx+1]
                    idx += 1
                else:
                    if tmp % (idx+1) != 0: tmp += 1
            else:
                if tmp % (idx+1) != 0: tmp += 1
            answer = max(answer,tmp)
    else:
        print(answer)