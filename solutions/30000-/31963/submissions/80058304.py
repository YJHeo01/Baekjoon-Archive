def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer = 0
    for i in range(1,n):
        while True:
            if array[i] >= array[i-1]:break
            answer += 1
            array[i] *= 2
    print(answer)

if __name__ == "__main__":
    main()