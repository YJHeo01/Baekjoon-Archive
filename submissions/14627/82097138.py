import sys

input = sys.stdin.readline

def main():
    s,c = map(int,input().split())
    array = []
    for _ in range(s):
        array.append(int(input()))
    target_length = 0
    left, right = 1, max(array)
    while left <= right:
        mid = (left+right) // 2
        tmp = 0
        for i in array:
            tmp += i // mid
        if tmp >= c:
            left = mid + 1
            target_length = mid
        else:
            right = mid - 1
    answer = sum(array) - target_length * c
    print(answer)

if __name__ == "__main__":
    main()