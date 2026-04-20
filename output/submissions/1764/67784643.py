a, b = map(int,input().split())
dm = []
bm = []
cnt = 0
dbj = []
for i in range(a):
    dm.append(input())
for i in range(b):
    bm.append(input())
for i in range(a):
    for j in range(b):
        if dm[i] == bm[j]:
            dbj.append(dm[i])
            cnt += 1

dbj.sort()

print(cnt)
for i in range(cnt):
    print(dbj[i])