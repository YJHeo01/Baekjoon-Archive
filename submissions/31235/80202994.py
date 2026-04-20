def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer = 1
    max_value = array[0]
    max_idx = 0
    for i in range(1,n):
        if array[i] > max_value:
            answer = max(answer,i-max_idx)
            max_value = array[i]
            max_idx = i
    print(answer)

if __name__ == "__main__":
    main()