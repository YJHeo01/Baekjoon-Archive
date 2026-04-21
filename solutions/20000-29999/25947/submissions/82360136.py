import sys

input = sys.stdin.readline

def main():
    n,b,a = map(int,input().split())
    cost = sorted(list(map(int,input().split())))
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + cost[i]
    for i in range(a):
        if (prefix_sum[i+1] - prefix_sum[0]) // 2 > b:
            print(i)
            return
    for i in range(a,n):
        if (prefix_sum[i+1] - prefix_sum[i-a]) // 2 + prefix_sum[i-a+1] - prefix_sum[0] > b:
            print(i)
            return
    print(n)

if __name__ == "__main__":
    main()