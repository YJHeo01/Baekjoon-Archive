def main():
    e,s,m = map(int,input().split())
    answer = 1
    a,b,c = 1,1,1
    while True:
        if a == e and s == b and c == m:
            break
        answer += 1
        a += 1; b += 1; c += 1
        if a > 15: a = 1
        if b > 28: b = 1
        if c > 19: c = 1
    print(answer)

if __name__ == "__main__":
    main()