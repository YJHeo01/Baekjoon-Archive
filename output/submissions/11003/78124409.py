import heapq

INF = int(1e9)

def main():    
    array = list(map(int,input().split()))
    solution(array)

def solution(array):
    q = []
    min_value = INF
    for i in range(l):
        if min_value > array[i]: min_value = array[i]; q = []
        heapq.heappush(q,(array[i],i))
        print(min_value,end=" ")
    for i in range(l,n):
        if min_value >= array[i]: q = []
        heapq.heappush(q,(array[i],i))
        while True:
            value, idx = heapq.heappop(q)
            if idx > i - l:
                min_value = value
                heapq.heappush(q,(value,idx))
                break
        print(min_value,end=" ")

if __name__ == "__main__":
    n,l = map(int,input().split())
    main()