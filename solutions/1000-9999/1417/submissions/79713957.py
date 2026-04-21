def main():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(int(input()))
    answer = 0
    while True:
        max_idx = -1
        max_value = array[0]
        for i in range(1,n):
            if array[i] >= max_value:
                max_value = array[i]
                max_idx = i
        if max_idx == -1:break
        answer += 1
        array[0] += 1
        array[max_idx] -= 1
    print(answer)

if __name__  == "__main__":
    main()