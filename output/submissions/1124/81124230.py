def main():
    a,b = map(int,input().split())
    INF = 100001
    prime = [True] * INF
    prime_cnt = [1] * INF
    prefix_sum = [0] * INF
    for i in range(2,INF):
        prefix_sum[i] = prefix_sum[i-1]
        
        if prime[i] == False:
            if prime[prime_cnt[i]] == True: prefix_sum[i] += 1
            continue
        
        prefix_sum[i] = prefix_sum[i-1]
        prime_cnt[i] = 1
        
        for j in range(i+i,INF,i):
            prime[j] = False
            prime_cnt[j] = prime_cnt[j//i] + 1
    
    print(prefix_sum[b]-prefix_sum[a-1])
            
        
if __name__ == "__main__":
    main()