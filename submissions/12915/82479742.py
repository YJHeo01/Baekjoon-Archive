e,em,m,mh,h = map(int,input().split())
answer = min(e,m,h)
for e_em in range(em+1):
    tmp = 0
    for h_mh in range(mh+1):
        new_e, new_m, new_h = e + e_em,m-h_mh-e_em+em+mh,h+h_mh
        new_tmp = min(new_e,new_m,new_h)
        if new_tmp > tmp:
            tmp = new_tmp
        else:
            break
    answer = max(answer,tmp)
print(answer)
