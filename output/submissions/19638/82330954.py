import heapq, sys

input = sys.stdin.readline

def main():
    n,h,t = map(int,input().split())
    q= []
    for _ in range(n):
        heapq.heappush(q,int(input())*-1)
    for i in range(t):
        tmp = heapq.heappop(q)
        if h > tmp:
            print("YES")
            print(i)
            return
        elif tmp == 1:
            print("NO")
            print(1)
            return
        else:
            heapq.heappush(q,(tmp//2)*-1)
    tmp = heapq.heappop(q)
    tmp *= -1
    if h > tmp:
        print("YES")
        print(t)
    else:
        print("NO")
        print(tmp)

if __name__ == "__main__":
    main()