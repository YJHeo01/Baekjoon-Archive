def cal(a,b,m,n):
    cnt = 0
    for i in range(0,n):
        if a[i] != b[i+m]: cnt+=1
    return cnt

a, b = list(input().split())
a_ = len(a)
b_ = len(b)
idx = b_ - a_
cnt = 51
for i in range(0,idx+1):
    tmp = cal(a,b,i,a_)
    if cnt > tmp:
        cnt = tmp
print(cnt)