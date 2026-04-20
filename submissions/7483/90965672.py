while True:

    n = int(input())
    if n == 0: break
    array = list(map(int,input().split()))

    cnt = dict()
    arr = []
    for i in array:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
            arr.append(i)
    arr.sort()
    length = len(arr)

    for i in range(length):
        x = arr[i]
        if cnt[x] == 0: continue
        if i + 1 != length and arr[i+1] == x+1:
            if cnt[x] + cnt[arr[i+1]] == n:
                for _ in range(cnt[arr[i+1]]):
                    print(arr[i+1],end=" ")
                n -= cnt[arr[i+1]]
                cnt[arr[i+1]] = 0
            else:
                for _ in range(cnt[x]):
                    print(x,end=" ")
                print(arr[i+2],end=" ")
                cnt[arr[i+2]] -= 1
                n -= 1
                n -= cnt[x]
                cnt[x] = 0
                continue
        for _ in range(cnt[x]):
            print(x,end=" ")
        n -= cnt[x]
        cnt[x] = 0
    print()