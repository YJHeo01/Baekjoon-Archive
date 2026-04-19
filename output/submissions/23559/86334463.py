import sys, heapq

input = sys.stdin.readline

def main():
    q = []
    n,x = map(int,input().split())
    answer = 0
    for _ in range(n):
        a,b = map(int,input().split())
        heapq.heappush(q,(b-a,a,b))
    for i in range(n):
        tmp,a,b = heapq.heappop(q)
        if tmp >= 0 or 5000 + (n-1-i) > x:
            answer += b
            break
        answer += a
        x -= 5000
    while q:
        tmp,a,b = heapq.heappop(q)
        answer += b
    print(answer)

if __name__ == "__main__":
    main()