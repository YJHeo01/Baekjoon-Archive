import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    tmp = {}
    for _ in range(n):
        trash, name = input().rstrip().split('.')
        if name in tmp:
            tmp[name] += 1
        else:
            tmp[name] = 1
    q = []
    for name in tmp:
        heapq.heappush(q,(name,tmp[name]))
    while q:
        name, cnt = heapq.heappop(q)
        print(name,cnt)

if __name__ == "__main__":
    main()