import sys

input = sys.stdin.readline

def main():
    n,t = map(int,input().split())
    happy = [0] * 1001
    for _ in range(n):
        k = int(input())
        for _ in range(k):
            a,b = map(int,input().split())
            for i in range(a,b):
                happy[i] += 1
    prefix_sum = [0] * 1001
    for i in range(1000):
        prefix_sum[i+1] = prefix_sum[i] + happy[i]
    end = t
    for i in range(t,1001):
        if prefix_sum[i] - prefix_sum[i-t] > prefix_sum[end] - prefix_sum[end-t]: end = i
    print(end-t,end)

if __name__ == "__main__":
    INF = int(1e9)
    main()