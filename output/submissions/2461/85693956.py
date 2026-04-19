import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    if n == 1:
        print(0)
        return
    array = [sorted(list(map(int,input().split()))) for _ in range(n)]
    max_value = 0
    for i in range(n): max_value = max(max_value,array[i][0])
    q = []
    for i in range(n):
        for j in range(m-1):
            heapq.heappush(q,(array[i][j],array[i][j+1]))
        heapq.heappush(q,(array[i][m-1],INF))
    answer = INF
    while q:
        min_value, next_value = heapq.heappop(q)
        answer = min(answer,max_value-min_value)
        max_value = max(max_value,next_value)
        if max_value == INF: break
    print(answer)

if __name__ == "__main__":
    INF = int(1e9) + 1
    main()