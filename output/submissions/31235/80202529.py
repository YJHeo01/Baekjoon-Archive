def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer, tmp = 1,1
    for i in range(1,n):
        answer = max(answer,tmp)
        if array[i] >= array[i-1]:
            tmp = 1
        else:
            tmp += 1
    print(answer)

if __name__ == "__main__":
    main()