import sys

input = sys.stdin.readline

def main():
    prime = [True] * INF
    prime[0], prime[1] = False, False
    prefix_sum_prime_cnt = [0] * INF
    cur_prime_cnt = 0
    prefix_sum_prime_squared_sum = [0] * INF
    cur_prime_squared_sum_cnt = 0
    for i in range(INF):
        if prime[i] == True:
            cur_prime_cnt += 1
            if i % 4 == 1: cur_prime_squared_sum_cnt += 1
            for j in range(i*2,INF,i):
                prime[j] = False
        prefix_sum_prime_cnt[i] = cur_prime_cnt
        prefix_sum_prime_squared_sum[i] = cur_prime_squared_sum_cnt
 
    while True:
        l,u = map(int,input().split())
        if l == -1 and u == -1: return
        print(l,u,end=" ")
        l,u = max(l,1), max(u,1)
        x = prefix_sum_prime_cnt[u] - prefix_sum_prime_cnt[l-1]
        y = prefix_sum_prime_squared_sum[u] - prefix_sum_prime_squared_sum[l-1]
        print(x,y)

if __name__ == "__main__":
    INF = 1000001
    main()