import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = sorted(list(map(int,input().split())))
    q = []
    for i in range(n-1):
        while True:
            if array[i] * 2 >= array[n-1]:
                heapq.heappush(q,(array[i]*2-array[n-1],i,array[i]*2))
                heapq.heappush(q,(array[n-1]-array[i],i,array[i]))
                break
            array[i] *= 2
    max_value, min_value = array[n-1], array[n-1]
    visited = [False] * n
    while q:
        tmp, idx, value = heapq.heappop(q)
        if visited[idx]: continue
        visited[idx] = True
        max_value, min_value = max(max_value,value), min(min_value,value)
    print(max_value-min_value)
        
if __name__ == "__main__":
    main()