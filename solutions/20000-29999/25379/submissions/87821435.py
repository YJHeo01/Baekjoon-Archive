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
        
first_odd = n
first_cou = n

for i in range(n-1,-1,-1):
    if a[i] % 2 == 0:
        first_cou = i
    else:
        first_odd = i

tmp_c,tmp_d = 0,0

for i in range(n-1,-1,-1):
    if a[i] % 2 == 0:
        if first_odd > i:
            continue
        tmp_c += (i-first_odd)
    else:
        if first_cou > i: continue
        tmp_d += (i-first_cou)
    
print(min(tmp_a,tmp_b,tmp_c,tmp_d))