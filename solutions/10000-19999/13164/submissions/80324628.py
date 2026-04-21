import heapq

def main():
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    answer = 0
    q = []
    for i in range(1,n):
        value = array[i] - array[i-1]
        answer += value
        heapq.heappush(q,-value)
    for _ in range(k-1):
        answer += heapq.heappop(q)
    print(answer)

if __name__ == "__main__":
    main()