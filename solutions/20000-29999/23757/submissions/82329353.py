import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    tmp = list(map(int,input().split()))
    q = []
    for i in tmp:
        heapq.heappush(q,-i)
    print(solution(q))
    
def solution(q):
    for i in list(map(int,input().split())):
        cnt = heapq.heappop(q)
        cnt += i
        if cnt > 0:
            return 0
        heapq.heappush(q,cnt)
    return 1

if __name__ == "__main__":
    main()