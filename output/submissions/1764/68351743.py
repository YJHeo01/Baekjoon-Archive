import sys
n,m= map(int,input().split())
d = [ [] for _ in range(26)]
b = [ [] for _ in range(26)]
d_cnt = [0] * 26
b_cnt = [0] * 26
answer = []
input = sys.stdin.readline
for i in range(n):
    tmp = input()
    d[ord(tmp[0])-ord('a')].append(tmp)
    d_cnt[ord(tmp[0])-ord('a')] += 1
cnt = 0
dbj = 0
for i in range(m):
    tmp = input()
    b[ord(tmp[0])-ord('a')].append(tmp)
    b_cnt[ord(tmp[0])-ord('a')] += 1

for i in range(26):
    for j in range(d_cnt[i]):
        for k in range(b_cnt[i]):
            if d[i][j] == b[i][k]:
                dbj = 1
                break
        if dbj == 1:
            d[i][j].rstrip()
            answer.append(d[i][j])
            cnt += 1
            dbj = 0

print(cnt)
answer.sort()
for i in range(cnt):
    print(answer[i].rstrip())