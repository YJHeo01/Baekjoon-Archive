def main():
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    left, right = 0,max(array)
    answer = 10000
    while left<=right:
        mid = (left+right) // 2
        idx,cnt = 0,1
        max_value = 0;min_value = 10000
        while True:
            if idx >= n:break
            max_value = max(max_value,array[idx])
            min_value = min(min_value,array[idx])
            if max_value - min_value > mid:
                cnt += 1
                max_value,min_value = array[idx],array[idx]
            idx += 1
        if cnt > m:
            left = mid +1
        else:
            answer = mid
            right = mid - 1
    print(answer)

if __name__ == "__main__":
    main()