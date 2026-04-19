import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    if n == 1:
        print(array[0][2])
        return
    dp = [0] * n
    dp[0], dp[1] = array[0][2], max(array[0][2],array[1][2])
    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2]+array[i][2])
    print(dp[n-1])

if __name__ == "__main__":
    main()