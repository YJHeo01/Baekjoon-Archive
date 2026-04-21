d,p,q = map(int,input().split())

def solution(p_min_cnt,p_max_cnt):
    mid = (p_max_cnt+p_min_cnt) // 2
    ret_value = mid * p + q_cnt(d-p*mid) * q
    if p_min_cnt == mid or p_max_cnt == mid: return ret_value
    l_mid = (p_min_cnt+mid) // 2
    if ret_value >= l_mid + q_cnt(d-p*l_mid):
        ret_value = min(ret_value,solution(p_min_cnt,mid))
    r_mid = (mid+p_max_cnt) // 2
    if ret_value >= r_mid + q_cnt(d-p*r_mid):
        ret_value = min(ret_value,solution(mid,p_max_cnt))
    return ret_value
    
def q_cnt(value):
    if value <= 0: return 0
    ret_value = value // q
    if value % q != 0: ret_value += 1
    return ret_value

answer = solution(0,d)

print(answer)