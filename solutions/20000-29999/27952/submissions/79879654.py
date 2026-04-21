def main():
    answer = 0
    weight = 0
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):
        weight += b[i]
        if weight < a[i]:
            answer = -1
            break
    if answer != -1:
        answer = (weight-a[-1]) // x
    print(answer)


if __name__ == "__main__":
    main()