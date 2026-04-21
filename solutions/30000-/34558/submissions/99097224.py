import sys

input = sys.stdin.readline

def main():
    n = int(input())
    INF = 2000001
    seive = [True] * INF
    prime = []
    prime_idx = -1
    max_prime_idx = [0] * INF
    min_prime_idx = [INF] * INF
    for i in range(2,INF):
        if seive[i] == True:
            prime_idx += 1
            prime.append(i)
            for j in range(i+i,INF,i):
                seive[j] = False
        max_prime_idx[i] = prime_idx
    for i in range(INF-1,1,-1):
        min_prime_idx[i] = prime_idx
        if seive[i] == True:
            prime_idx -= 1
    for _ in range(n):
        a,b = map(int,input().split())
        #print(max_prime_idx[b])
        if seive[a] == False: a = prime[min_prime_idx[a]+1]
        if b < prime[min_prime_idx[a]] or (min_prime_idx[a]-max_prime_idx[b]) % 2 == 1:
            print("-1")
        else:
            print(prime[(min_prime_idx[a]+max_prime_idx[b])//2])

if __name__ == "__main__":
    main()