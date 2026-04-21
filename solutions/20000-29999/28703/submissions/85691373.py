def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    array = sorted(list(map(int,input().split())))
    answer = array[n-1] - array[0]
    same_cnt = 0
    while True:
        break_check = True
        while True:
            if array[0] * 2 > array[1]:
                break
            array[0] <<= 1
        if array[n-1] - array[0] <= answer:
            if array[n-1] - array[0] == answer: same_cnt += 1
            else: same_cnt = 0
            answer = array[n-1] - array[0]
            break_check = False
        array[0] <<= 1
        for i in range(1,n):
            if array[i-1] <= array[i]: break
            array[i], array[i-1] = array[i-1], array[i]
        if array[n-1] - array[0] <= answer:
            if array[n-1] - array[0] == answer: same_cnt += 1
            else: same_cnt = 0
            answer = array[n-1] - array[0]
            break_check = False
        if break_check or same_cnt >= 5: break
        
    print(answer)

if __name__ == "__main__":
    main()