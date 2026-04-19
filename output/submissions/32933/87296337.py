def main():
    n,m,k = map(int,input().split())
    profit = [0] * (m+1)
    for _ in range(k):
        a,b,c = map(int,input().split())
        for i in range(a,m+1):
            for j in range(m):
                if i + j * b > m: break
                profit[i+j*b] = max(profit[i+j*b],profit[i-a]+c + c*j)
    print(n*max(profit))

if __name__ == "__main__":
    main()