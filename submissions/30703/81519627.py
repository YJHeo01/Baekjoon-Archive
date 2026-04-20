def main():
    n = int(input())
    init = list(map(int,input().split()))
    target = list(map(int,input().split()))
    change = list(map(int,input().split()))
    modu = [False,False]
    max_value = 0
    for i in range(n):
        if (init[i]-target[i]) % change[i] != 0:
            print(-1)
            return
        value = abs((init[i]-target[i]) // change[i])
        modu[value%2] = True
        max_value = max(max_value,value)
    if modu[0] == True and modu[1] == True:
        print(-1)
    else:
        print(max_value)

if __name__ == "__main__":
    main()