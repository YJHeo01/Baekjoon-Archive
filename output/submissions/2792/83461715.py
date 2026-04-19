import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    jewel = [int(input()) for _ in range(m)]
    answer = 10 ** 9
    left, right = 1,answer
    while left <= right:
        mid = (left+right) // 2
        tmp = 0
        for i in jewel:
            tmp += (i//mid)
            if i % mid != 0: tmp += 1
        if tmp <= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)

if __name__ == "__main__":
    main()