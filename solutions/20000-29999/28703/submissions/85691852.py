def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    array = sorted(list(map(int,input().split())))
    answer = array[n-1] - array[0]
    original_max_value = array[n-1]
    while True:
        while True:
            if array[0] * 2 > array[1]:
                break
            array[0] <<= 1
        if array[n-1] - array[0] <= answer:
            answer = array[n-1] - array[0]
        array[0] <<= 1
        for i in range(1,n):
            if array[i-1] <= array[i]: break
            array[i], array[i-1] = array[i-1], array[i]
        if array[n-1] - array[0] <= answer:
            answer = array[n-1] - array[0]
        if array[0] > original_max_value: break
    print(answer)

if __name__ == "__main__":
    main()