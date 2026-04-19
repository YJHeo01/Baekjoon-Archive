def main():
    n = int(input())
    init_array = list(map(int,input().split()))
    INF = int(1e9)
    answer = INF
    for i in range(-1,2):
        for j in range(-1,2):
            array = []
            for value in init_array: array.append(value)
            tmp = 0
            if i != 0: tmp += 1
            if j != 0: tmp += 1
            array[0] += i; array[1] += j
            for k in range(2,n):
                if array[k] + 1 - array[k-1] == array[1] - array[0]:
                    array[k] += 1
                    tmp += 1
                elif array[k] - 1 - array[k-1] == array[1] - array[0]:
                    array[k] -= 1
                    tmp += 1
                elif array[k] - array[k-1] == array[1] - array[0]:
                    continue
                else:
                    tmp = INF
                    break
            answer = min(answer,tmp)
    if answer >= INF:
        answer = -1
    print(answer)

if __name__ == "__main__":
    main()