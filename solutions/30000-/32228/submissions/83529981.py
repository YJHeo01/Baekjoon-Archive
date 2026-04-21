def main():
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    finish = True
    for i in range(2,n):
        if (array[i] - array[i-1]) % m != (array[i-1] - array[i-2]) % m:
            finish = False
            break
    if finish == True:
        print(1)
        return
    tmp = [0] * n
    for i in range(n):
        array[i] %= m
        tmp[i] = array[i]
    last_tmp = [0] * n
    for k in range(2,m+1):
        same_array = True
        for i in range(n):
            last_tmp[i] = tmp[i]
            tmp[i] *= array[i]
            tmp[i] %= m
            if tmp[i] != array[i] or last_tmp[i] != tmp[i]: same_array = False
        finish = True
        for i in range(2,n):
            if (tmp[i] - tmp[i-1]) % m != (tmp[i-1]-tmp[i-2]) % m:
                finish = False
                break
        if finish == True:
            print(k)
            return
        if same_array == True: break
    print(-1)


if __name__ == "__main__":
    main()