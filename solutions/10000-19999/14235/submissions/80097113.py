import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    present = []
    for _ in range(n):
        tmp = list(map(int,input().split()))
        if tmp[0] == 0:
            if present == []:
                print(-1)
            else:
                print(-heapq.heappop(present))
        else:
            for i in tmp[1:]:
                heapq.heappush(present,-i)

if __name__ == "__main__":
    main()