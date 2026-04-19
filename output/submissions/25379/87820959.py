n = int(input())

a = list(map(int,input().split()))

last_odd = -1
last_cou = -1

for i in range(n):
    if a[i] % 2 == 0:
        last_cou = i
    else:
        last_odd = i

tmp_a, tmp_b = 0,0

for i in range(n):
    if a[i] % 2 == 0:
        if last_odd < i: continue
        tmp_a += (last_odd-i)
    else:
        if last_cou < i:continue
        tmp_b += (last_cou-i)
    
print(min(tmp_a,tmp_b))