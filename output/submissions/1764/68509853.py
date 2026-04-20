import sys
input = sys.stdin.readline

n, m=map(int,input().split())


hash_table = [[]for _ in range(66)]    
for i in range(n):
    tmp = input().rstrip()
    hash_table[ord(tmp[0])-ord('a')+2*len(tmp)].append(tmp)
answer = []
cnt = 0
for j in range(m):
    tmp = input().rstrip()
    if tmp in hash_table[ord(tmp[0])-ord('a')+2*len(tmp)]:
        answer.append(tmp)
        cnt += 1

print(cnt)
answer.sort()
for i in answer:
    print(i)