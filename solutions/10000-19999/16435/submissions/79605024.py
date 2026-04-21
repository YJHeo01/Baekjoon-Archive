def main():
    n,l = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort()
    for i in range(n):
        if l >= array[i]: l += 1
        else: break
    print(l)

if __name__ == "__main__":
    main()