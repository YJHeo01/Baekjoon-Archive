def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer, tmp = 1,1
    for i in range(1,n):
        if array[i-1] > array[i]:
            tmp += 1
        elif array[i] > array[i-1]:
            tmp = 1
        else:
            if tmp == 1: tmp = 1
            else: tmp += 1
        answer = max(answer,tmp)
    print(answer)

if __name__ == "__main__":
    main()