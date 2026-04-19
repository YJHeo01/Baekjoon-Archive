def main():
    n = int(input())
    array = list(map(int,input().split()))
    array[0] += 100000
    array[n-1] -= 100000
    for i in range(1,n//2):
        tmp = min(100000,array[i-1]-array[i],array[n-1-i]-array[n-i])
        array[i] += tmp
        array[n-1-i] -= tmp
    print(n//2)
    for i in array:
        print(i,end=" ")

if __name__ == "__main__":
    main()