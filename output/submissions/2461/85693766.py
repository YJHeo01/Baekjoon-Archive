import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    array = [sorted(list(map(int,input().split()))) for _ in range(n)]
    max_value = 0
    for i in range(n): max_value = max(max_value,array[i][0])
    answer = int(1e9)
    q = []
    for i in range(n):
        for j in range(m-1):
            heapq.heappush(q,(array[i][j],array[i][j+1],i,j))
        heapq.heappush(q,(array[i][m-1],int(1e9),i,j))
    answer = int(1e9)
    while q:
        min_value, next_value, i, j = heapq.heappop(q)
        answer = min(answer,max_value-min_value)
        max_value = max(max_value,next_value)
    print(answer)

if __name__ == "__main__":
    main()