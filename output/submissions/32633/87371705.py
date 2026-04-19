import sys

input = sys.stdin.readline

def main():
    n,l = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    prime_list = []
    prime = [True] * INF
    for i in range(2,INF):
        if prime[i]:
            prime_list.append(i)
            for j in range(i,INF,i):
                prime[j] = False
    prime_cnt = len(prime_list)
    prime_of_t = [0] * prime_cnt
    prime_of_no = [0] * prime_cnt
    for i in range(n):
        tmp = a[i]
        for j in range(prime_cnt):
            cnt = 0
            while True:
                if tmp % prime_list[j] != 0:break
                tmp //= prime_list[j]
                cnt += 1
            if b[i] == 1:
                prime_of_t[j] = max(prime_of_t[j],cnt)
            else:
                prime_of_no[j] = max(prime_of_no[j],cnt)
    t = -1
    for i in range(prime_cnt):
        if prime_of_t[i] < prime_of_no[i]: t = 1
    if sum(b) == n: t = 1
    if t != -1:
        for i in range(prime_cnt):
            for _ in range(prime_of_t[i]):
                t *= prime_list[i]
    if t > l: t = -1
    print(t)

if __name__ == "__main__":
    INF = 10001
    main()