import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    n = int(input())
    q_a, q_b = get_q(n)
    d = int(input())
    answer = max(solution(q_a,d),solution(q_b,d))
    print(answer)

def get_q(n):
    q_a,q_b = [],[]
    for _ in range(n):
        a,b = map(int,input().split())
        if a< b:
            heapq.heappush(q_a,(a,b))
            heapq.heappush(q_b,(-b,-a))   
        else:
            heapq.heappush(q_a,(b,a))
            heapq.heappush(q_b,(-a,-b))
    return q_a, q_b

def solution(q,d):
    first_start = init_start(q,d)
    if first_start == INF:
        return 0
    start = first_start; ret_value = 1; tmp = 1; next_start_q = []
    while q:
        left, right = heapq.heappop(q)
        if right - left > d:
            continue
        heapq.heappush(next_start_q,left)
        if start + d >= right:
            tmp += 1
            ret_value = max(ret_value,tmp)
            continue         
        while next_start_q:
            tmp -= 1
            new_start = heapq.heappop(next_start_q)
            if new_start + d >= right:
                tmp += 1
                break
    return ret_value

def init_start(q,d):
    ret_value = INF
    while q:
        left, right = heapq.heappop(q)
        if right - left <= d:
            ret_value = left
            break
    return ret_value

if __name__ == "__main__":    
    main()