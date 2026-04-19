import math

def main():
    n,a,b,c,d = map(int,input().split())
    if b / a < d / c:
        a,b,c,d = c,d,a,b
    answer = INF
    second_rose_cnt = 0
    while True:
        tmp_value = max(0,math.ceil((n-c*second_rose_cnt)/a)) * b + second_rose_cnt * d
        if answer > tmp_value:
            answer = tmp_value
        else:
            break
        second_rose_cnt += 1
    print(answer)

if __name__ == "__main__":
    INF = int(1e18)
    main()