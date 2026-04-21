def main():
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    answer = 2 *int(1e9) + 1
    for i in range(3,n):
        answer = min(answer,abs(array[i]+array[i-3]-array[i-2]-array[i-1]))
    print(answer)

if __name__ == "__main__":
    main()