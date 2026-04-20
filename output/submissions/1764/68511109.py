import sys
input = sys.stdin.readline

n, m=map(int,input().split())


hash_table = [[]for _ in range(1000)]    
for i in range(n):
    tmp = input().rstrip()
    l = len(tmp)
    sum = 0
    for j in range(l):
        sum += (ord(tmp[0])-ord('a'))
    sum %= 1000
    hash_table[sum].append(tmp)
answer = []
cnt = 0
for i in range(m):
    tmp = input().rstrip()
    sum = 0
    l = len(tmp)
    for j in range(l):
        sum += (ord(tmp[0])-ord('a'))
    sum %= 1000
    if tmp in hash_table[sum]:
        answer.append(tmp)
        cnt += 1

print(cnt)
answer.sort()
for i in answer:
    print(i)