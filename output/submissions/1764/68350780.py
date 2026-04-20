n,m= map(int,input().split())
d = []
b = []
answer = []
for i in range(n):
    tmp = input()
    d.append(tmp)
cnt = 0
dbj = 0
for i in range(m):
    tmp = input()
    b.append(tmp)

for i in range(n):
    for j in range(m):
        if d[i] == b[j]:
            dbj = 1
            break
    if dbj == 1:
        answer.append(d[i])
        cnt += 1
        dbj = 0

print(cnt)
answer.sort()
for i in range(cnt):
    print(answer[i])