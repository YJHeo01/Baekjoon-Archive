def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    array = sorted(list(map(int,input().split())))
    answer = array[n-1] - array[0]
    max_value_idx = n-1
    while True:
        min_value_idx = max_value_idx
        for i in range(n):
            while True:
                if array[i] * 2 > array[max_value_idx]:
                    break
                array[i] *= 2
            if array[min_value_idx] > array[i]:
                min_value_idx = i
        answer = min(answer,array[max_value_idx]-array[min_value_idx])
        array[min_value_idx] *= 2
        if array[min_value_idx] > array[max_value_idx]:
            max_value_idx = min_value_idx
        if min_value_idx == n-1: break
    print(answer)

if __name__ == "__main__":
    main()