import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    array = [int(input()) for _ in range(n)]
    answer = 0
    left, right = 1,max(array)
    while left <= right:
        mid = (left+right) // 2
        tmp = 0
        for i in array:
            tmp += i // mid
        if tmp >= k:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)

if __name__ == "__main__":
    main()