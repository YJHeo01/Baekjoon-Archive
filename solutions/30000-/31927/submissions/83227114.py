def main():
    n = int(input())
    array = list(map(int,input().split()))
    k = n // 2
    for i in range(n//2):
        tmp = 500000-5000*i
        array[i] += tmp
        array[n-1-i] -= tmp
    print(k)
    for i in array:
        print(i,end=" ")

if __name__ == "__main__":
    main()