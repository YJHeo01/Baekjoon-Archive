import heapq

def main():
    array = []
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    k = solution(array,n,a,m,b)
    print(k)
    print(*array)

def solution(array,n,a,m,b):
    k = 0
    a_prior_q, b_prior_q = [], []
    for i in range(n):
        heapq.heappush(a_prior_q,(-a[i],i))
    for i in range(m):
        heapq.heappush(b_prior_q,(-b[i],i))
    a_last_idx, b_last_idx = -1,-1
    a_value, a_idx = heapq.heappop(a_prior_q)
    b_value, b_idx = heapq.heappop(b_prior_q)
    while True:
        while True:
            if a_last_idx < a_idx: break
            if a_prior_q == []: return k
            a_value, a_idx = heapq.heappop(a_prior_q)
        while True:
            if b_last_idx < b_idx: break
            if b_prior_q == []: return k
            b_value, b_idx = heapq.heappop(b_prior_q)
        if a_value < b_value:
            
            if a_prior_q == []:break
            a_value, a_idx = heapq.heappop(a_prior_q)
        elif b_value < a_value:
            if b_prior_q == []:break
            b_value, b_idx = heapq.heappop(b_prior_q)
        else:
            array.append(-b_value)
            k += 1
            a_last_idx, b_last_idx = a_idx, b_idx
    return k

if __name__ == "__main__":
    main()