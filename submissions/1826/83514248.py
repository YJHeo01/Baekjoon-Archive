import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = sorted([list(map(int,input().split())) for _ in range(n)])
    l,p = map(int,input().split())
    q = []
    impossible = False
    cnt = 0
    for a,b in array:
        while True:
            if p >= a: break
            if q == []:
                impossible = True
                break
            energy = heapq.heappop(q)
            cnt += 1
            p -= energy
        heapq.heappush(q,-b)
    while True:
        if p >= l: break
        if q == []:
            impossible = True
            break
        energy = heapq.heappop(q)
        cnt += 1
        p -= energy
    if impossible == True: cnt = -1
    print(cnt)

if __name__ == "__main__":
    main()