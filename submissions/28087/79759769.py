import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    array = []
    for i in range(1,m+1):
        array.append([int(input()),i])
    array.sort(reverse=True)
    value = 0
    idx = m
    left, right = 0,m-1
    while left <= right:
        mid = (left+right) // 2
        if array[mid][0] <= 2 * n:
            idx = mid
            right = mid - 1
        else:
            left = mid + 1
    answer = []
    while True:
        tmp = value + array[idx][0]
        if tmp <= 2 * n:
            value = tmp
            answer.append(array[idx][1])
        if value >= n:
            break
        idx += 1
    print(len(answer))
    for i in answer:
        print(i)

if __name__  == "__main__":
    main()