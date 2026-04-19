def main():
    n,l = map(int,input().split())
    array = list(map(int,input().split()))
    b = list(map(int,input().split()))
    t = 1

    for i in range(n):
        if b[i] == 1:
            gcd = euclidean(max(array[i],t),min(array[i],t))
            t = t * array[i] // gcd

    if t > l: t = -1
    for i in range(n):
        if t == -1: break
        if b[i] == 0 and t % array[i] == 0: t = -1
    print(t)


def euclidean(a,b):
    if b == 0: return a
    return euclidean(b,a%b)

if __name__ == "__main__":
    main()