def main():
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    answer = 2 *int(1e9) + 1
    for a in range(3,n):
        for b in range(2,a):
            for c in range(1,b):
                for d in range(c):
                    answer = min(answer,abs(array[a]+array[d]-array[b]-array[c]))
    print(answer)

if __name__ == "__main__":
    main()