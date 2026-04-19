def main():
    n,a,b,c,d = map(int,input().split())
    if c / d > a / b:
        a,b,c,d = c,d,a,b
    answer = n // a
    if n % a != 0: answer += 1
    answer *= b
    c_cnt = 1
    while True:
        if c*c_cnt > n:break
        tmp = (n-c_cnt*c)//a
        if (n-c_cnt*c)%a != 0:
            tmp += 1
        if answer > c_cnt*d + tmp * b:
            answer = c_cnt*d + tmp * b
        else:break
        c_cnt += 1
    print(answer)

if __name__ == "__main__":
    INF = int(1e9)
    main()