for _ in range(int(input())):
    arr_set = set([])
    n = int(input())
    arr = list(map(int,input().split()))
    answer = 'ZERO'
    while True:
        arr_set.add(tuple(arr))
        tmp = []
        for i in range(n-1):
            tmp.append(abs(arr[i]-arr[i+1]))
        tmp.append(abs(arr[n-1]-arr[0]))
        arr = tmp
        if tuple(arr) in arr_set:
            for i in arr:
                if i != 0: 
                    answer = 'LOOP'
            break
    print(answer)