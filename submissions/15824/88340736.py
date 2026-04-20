import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = sorted(list(map(int,input().split())))
    answer = 0
    INF = 1000000007
    mul = 1
    for i in range(n):
        answer += array[i] * mul
        answer -= array[n-i-1] * mul
        mul *= 2; mul %= INF
        answer %= INF
    print(answer)
        
if __name__ == "__main__":
    main()