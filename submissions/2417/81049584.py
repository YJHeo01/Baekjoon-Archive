def main():
    n = int(input())
    answer = 0
    left, right = 0,n
    while left <= right:
        mid = (left+right) // 2
        if mid ** 2 >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)

if __name__ == "__main__":
    main()