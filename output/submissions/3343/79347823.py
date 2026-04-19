import math

def main():
    n,a,b,c,d = map(int,input().split())
    answer = math.ceil(n/a) * b
    c_cnt = 1
    while True:
        if c*c_cnt > n:break
        answer = min(answer,c_cnt*d + math.ceil((n-c_cnt*c)/a) * b)
        c_cnt += 1
    answer = min(answer,math.ceil(n/c)*d)
    print(answer)

if __name__ == "__main__":
    INF = int(1e9)
    main()