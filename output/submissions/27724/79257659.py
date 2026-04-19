def main():
    n,m,k = map(int,input().split())
    answer = 0; tmp = 1

    while True:
        if 2 ** tmp > k:break
        answer += 1; tmp += 1

    for _ in range(m):
        if 2 ** answer == n: break
        answer += 1
    print(answer)

if __name__ == "__main__":
    main()