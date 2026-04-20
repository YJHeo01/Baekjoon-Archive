def main():
    n,d = map(int,input().split())
    array = list(map(int,input().split()))
    cnt = [0] * (n+1)
    for i in array: cnt[i] += 1
    answer = 0
    for i in cnt:
        if i <= d: continue
        answer += i // d
    print(answer)

if __name__ == "__main__":
    main()