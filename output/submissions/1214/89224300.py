d,p,q = map(int,input().split())

if q > p: p,q = q,p

answer = int(1e18)

for i in range(min(d//p,q)+1):
    answer = min(answer,d+(q-(d-p*i)%q)%q)

answer = min(answer,d+(p-(d%p))%p)

print(answer)