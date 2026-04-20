d,p,q = map(int,input().split())

if q > p: p,q = q,p

if p % q == 0:
    answer = (d // q) * q
    if answer < d: answer += q
    print(answer)
    exit(0)

def solution(p_min_cnt,p_max_cnt):
    mid = (p_max_cnt+p_min_cnt) // 2
    ret_value = mid * p + q_cnt(d-p*mid) * q
    l_mid = (p_min_cnt+mid) // 2
    if ret_value >= l_mid + q_cnt(d-p*l_mid) and p_max_cnt != mid:
        ret_value = min(ret_value,solution(p_min_cnt,mid))
    r_mid = (mid+p_max_cnt) // 2
    if ret_value >= r_mid + q_cnt(d-p*r_mid) and p_min_cnt != mid:
        ret_value = min(ret_value,solution(mid,p_max_cnt))
    return ret_value
    
def q_cnt(value):
    if value <= 0: return 0
    ret_value = value // q
    if value % q != 0: ret_value += 1
    return ret_value

answer = solution(0,d//p+2)

print(answer)