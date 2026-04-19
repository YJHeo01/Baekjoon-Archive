def main():
    n = int(input())
    array = list(map(int,input().split()))
    INF = 10 ** 6
    print(n//2)
    for i in range(n//2):
        tmp = INF - 5000 * i
        array[i] += tmp
        array[n-1-i] -= tmp
        for value in array:
            print(value,end=" ")
        print()

if __name__ == "__main__":
    main()