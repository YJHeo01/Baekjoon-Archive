import sys

input = sys.stdin.readline

def main():
    n = int(input())
    small = [INF,INF,INF,INF]
    for _ in range(n):
        tmp = list(map(int,input().split()))
        for i in tmp:
            if small[3] > i:
                small[3] = i
                small.sort()
    bibim = []
    for i in range(4):
        for j in range(i):
            bibim.append(int(str(small[i])+str(small[j])))
            bibim.append(int(str(small[j])+str(small[i])))
    bibim.sort()
    print(bibim[2])

if __name__ == "__main__":
    INF = 1000010000
    main()