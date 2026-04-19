def main():
    answer = ["multiple","factor","neither"]
    while True:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            return
        state = 0
        if m > n:
            state = 1
            n,m = m,n
        if n % m != 0:
            state = 2
        print(answer[state])

if __name__ == "__main__":
    main()