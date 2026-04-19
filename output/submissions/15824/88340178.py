import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = sorted(list(map(int,input().split())))
    answer = 0
    INF = 1000000007
    for i in range(n):
        for j in range(i):
            answer += (array[i]-array[j]) << (i-j-1)
            answer %= INF
    print(answer)
        
if __name__ == "__main__":
    main()