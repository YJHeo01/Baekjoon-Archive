import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    ice = [0] * (1000001)
    for _ in range(n):
        g,x = map(int,input().split())
        ice[x] = g
    tmp = 0
    for i in range(2*k+1):
        tmp += ice[i]
    answer = tmp
    for right in range(2*k+1,1000001):
        left = right - 2 * k - 1
        tmp -= ice[left]
        tmp += ice[right]
        answer = max(answer,tmp)
    print(answer)

if __name__ == "__main__":
    main()