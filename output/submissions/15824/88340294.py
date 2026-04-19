import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = sorted(list(map(int,input().split())))
    answer = 0
    INF = 1000000007
    for i in range(n-1,-1,-1):
        answer += array[i] << i
        answer -= array[i] << (n-1-i)
        answer %= INF
    print(answer)
        
if __name__ == "__main__":
    main()