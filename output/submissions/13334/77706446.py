import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    n = int(input())
    q = get_q(n)
    d = int(input())
    answer = solution(q,d)
    print(answer)

def get_q(n):
    q = []
    for _ in range(n):
        a,b = map(int,input().split())
        if a< b:
            heapq.heappush(q,(a,b))
        else:
            heapq.heappush(q,(b,a))
    return q

def solution(q,d):
    start = init_start(q,d)
    if start == INF:
        return 0
    ret_value = 1; tmp = 1; next_start_q = []
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