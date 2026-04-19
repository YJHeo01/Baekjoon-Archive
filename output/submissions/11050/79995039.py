def main():
    n,k = map(int,input().split())
    answer = 1
    for i in range(1,n+1):
        answer *= i
    for i in range(1,k+1):
        answer = answer // i
    for i in range(1,n-k+1):
        answer = answer // i
    print(answer)

if __name__ == "__main__":
    main()