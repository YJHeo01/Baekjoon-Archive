import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    time_list = [int(input()) for _ in range(n)]
    left, right = 1,int(1e9) * n
    answer = right
    while left <= right:
        mid = (left+right) // 2
        tmp = 0
        for time in time_list:
            tmp += mid // time
        if tmp >= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)

if __name__ == "__main__":
    main()