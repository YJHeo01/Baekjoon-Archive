import sys

input = sys.stdin.readline

def main():
    m = int(input())
    f = [0] + list(map(int,input().split()))
    fx = [[0]*(m+1) for _ in range(21)]
    for i in range(1,m+1):
        fx[0][i] = f[i]
    for i in range(1,21):
        for j in range(1,m+1):
            fx[i][j] = fx[i-1][fx[i-1][j]]
    q = int(input())
    for _ in range(q):
        n,x = map(int,input().split())
        tmp = 1 << 20
        for i in range(20,-1,-1):
            if n >= tmp:
                x = fx[i][x]
                n -= tmp
            tmp >>= 1
        print(x)

if __name__ == "__main__":
    main()