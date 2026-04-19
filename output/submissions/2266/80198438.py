def main():
    n,k = map(int,input().split())
    print(E(n,k))

def E(n,k):
    return n // k + k - 1

if __name__ == "__main__":
    main()