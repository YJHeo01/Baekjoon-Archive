n,m = map(int,input().split())

value = []
for _ in range(n):
    p,l = map(int,input().split())
    tmp = sorted(map(int,input().split()),reverse=True)
    if l > p: value.append(0)
    else: value.append(tmp[l-1])
    
value.sort()

answer = 0

for i in value:
    if i > m or i > 36 or m == 0: break
    answer += 1
    m -= max(1,i)

print(answer)