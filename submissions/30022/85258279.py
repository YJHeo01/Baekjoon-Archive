import heapq, sys

input = sys.stdin.readline

def main():
    prior_q = []
    n,a,b = map(int,input().split())
    for _ in range(n):
        p,q = map(int,input().split())
        if p < q:
            heapq.heappush(prior_q,(q-p,p,q,1))
        else:
            heapq.heappush(prior_q,(p-q,p,q,2))
    answer = 0
    while prior_q:
        tmp, p, q, value = heapq.heappop(prior_q)
        if value == 1:
            if a >= 0:
                answer += p
                a -= 1
            else:
                answer += q
                b -= 1   
        else:
            if b >= 0:
                answer += q
                b -= 1
            else:
                answer += p
                a -= 1
    print(answer)

if __name__ == "__main__":
    main()