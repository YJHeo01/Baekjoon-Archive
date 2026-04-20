import sys

input = sys.stdin.readline

def main():
    prime = [True] * INF
    prime[0], prime[1] = False, False
    squared = [1]
    prefix_sum_prime_cnt = [0] * INF
    cur_prime_cnt = 0
    
    for i in range(2,INF):
        if i ** 2 < INF: squared.append(i**2)
        if prime[i] == True:
            cur_prime_cnt += 1
            for j in range(i*2,INF,i):
                prime[j] = False
        prefix_sum_prime_cnt[i] = cur_prime_cnt
    
    l = len(squared)
    squared_sum = [False] * INF
    for i in range(1,l):
        for j in range(i):
            if squared[i]+squared[j] >= INF or prime[squared[i]+squared[j]] == False: continue
            squared_sum[squared[i]+squared[j]] = True
    
    prefix_sum_prime_squared_sum = [0] * INF
    for i in range(1,INF):
        prefix_sum_prime_squared_sum[i] = prefix_sum_prime_squared_sum[i-1]
        if squared_sum[i] == True: prefix_sum_prime_squared_sum[i] += 1
    
    while True:
        l,u = map(int,input().split())
        if l == -1 and u == -1: return
        l,u = max(l,1), max(u,1)
        x = prefix_sum_prime_cnt[u] - prefix_sum_prime_cnt[l-1]
        y = prefix_sum_prime_squared_sum[u] - prefix_sum_prime_squared_sum[l-1]
        print(l,u,x,y)

if __name__ == "__main__":
    INF = 1000001
    main()