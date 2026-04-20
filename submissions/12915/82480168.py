e,em,m,mh,h = map(int,input().split())
answer = min(e,m,h)
for e_em in range(em+1):
    left, right = 0,mh
    while left <= right:
        h_mh = (left+right) // 2
        new_e, new_m, new_h = e + e_em, m + mh + em - e_em - h_mh, h + h_mh
        answer = max(answer,min(new_e,new_m,new_h))
        if new_h > new_m:
            right = h_mh - 1
        else:
            left = h_mh + 1
print(answer)