import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    answer = 0
    max_value = 0
    plus_q, minus_q = [], []
    for i in array:
        max_value = max(max_value,abs(i))
        if i > 0:
            heapq.heappush(plus_q,-i)
        else:
            heapq.heappush(minus_q,i)
    while plus_q:
        answer -= heapq.heappop(plus_q) * 2
        for _ in range(m-1):
            if plus_q == []: break
            heapq.heappop(plus_q)
    while minus_q:
        answer -= heapq.heappop(minus_q) * 2
        for _ in range(m-1):
            if minus_q == []: break
            heapq.heappop(minus_q)
    answer -= max_value
    print(answer)

if __name__ == "__main__":
    main()