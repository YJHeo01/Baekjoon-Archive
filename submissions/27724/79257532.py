def main():
    n,m,k = map(int,input().split())
    answer = 0
    tmp = 1
    while True:
        if k >= 2 ** tmp:
            answer += 1
            tmp += 1
        else:
            break
    answer += m
    for _ in range(m):
        if 2 ** answer > n:
            answer -= 1
        else:
            break
    print(answer)

if __name__ == "__main__":
    main()