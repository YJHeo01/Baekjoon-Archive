def main():
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    left, right = 0, array[n-1]
    answer = int(1e9) + 2
    while left <= right:
        max_price = (left+right) // 2
        group_cnt = 0
        start, end = 0,0
        price_sum = 0
        while True:
            if end == n:
                group_cnt += 1
                price_sum += array[end-1] - array[start]
                break
            if array[end] - array[start] > max_price:
                group_cnt += 1
                price_sum += array[end-1] - array[start]
                start = end
            else:
                end += 1
        if group_cnt > k:
            left = max_price + 1
        elif group_cnt < k:
            right = max_price - 1
        else:
            answer = min(answer,price_sum)
            right = max_price - 1
    print(answer)

if __name__ == "__main__":
    main()