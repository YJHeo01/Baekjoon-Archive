import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + array[i]
    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        print(prefix_sum[b]-prefix_sum[a-1])

if __name__ == "__main__":
    main()