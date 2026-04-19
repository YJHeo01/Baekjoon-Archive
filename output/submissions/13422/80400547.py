import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n,m,k = map(int,input().split())
        array = list(map(int,input().split()))
        if n == m:
            if sum(array) < k: print(1)
            else: print(0)
            continue
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + array[i]
        answer = 0
        for i in range(m,n+1):
            if k > prefix_sum[i] - prefix_sum[i-m]:
                answer += 1
        for i in range(1,m):
            if k > prefix_sum[n] + prefix_sum[i] - prefix_sum[n-(m-i)]:
                answer += 1
        print(answer)

if __name__ == "__main__":
    main()