import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = [0] + list(map(int,input().split()))
    q = []
    for i in range(1,n+1):
        heapq.heappush(q,(array[i],i))
    m = int(input())
    for _ in range(m):
        tmp = list(map(int,input().split()))
        if tmp[0] == 1:
            heapq.heappush(q,(tmp[2],tmp[1]))
            array[tmp[1]] = tmp[2]
        else:
            while True:
                value, idx = heapq.heappop(q)
                if array[idx] == value:
                    print(idx)
                    heapq.heappush(q,(value,idx))
                    break
    

if __name__ == "__main__":
    main()