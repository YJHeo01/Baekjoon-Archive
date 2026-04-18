import sys, math

INF = 200000

input = sys.stdin.readline

while True:
    tmp = input()
    if tmp[0] == '0': break
    n,q = map(int,tmp.split())

    arr = [0] + list(map(int,input().split()))

    for i in range(1,n+1):
        arr[i] += 100000

    answer = [0] * q

    query_s = []

    for idx in range(q):
        i,j = map(int,input().split())
        query_s.append((i,j,idx))

    blk = int(math.sqrt(n))

    query_s.sort(key=lambda x:(x[0]//blk,x[1] if (x[0] // blk) & 1 == 0 else -x[1]))

    left,right = 1,0

    max_cnt = 0
    
    cnt = [0] * (INF+1)
    info = [0] * (INF+1)

    for i,j,idx in query_s:
        while right < j:
            right += 1
            cnt[info[arr[right]]] -= 1
            info[arr[right]] += 1
            cnt[info[arr[right]]] += 1
            if info[arr[right]] > max_cnt: max_cnt = info[arr[right]]
        while right > j:
            cnt[info[arr[right]]] -= 1
            info[arr[right]] -= 1
            cnt[info[arr[right]]] += 1
            if cnt[max_cnt] == 0: max_cnt -= 1
            right -= 1
        while left < i:
            cnt[info[arr[left]]] -= 1
            info[arr[left]] -= 1
            cnt[info[arr[left]]] += 1
            if cnt[max_cnt] == 0: max_cnt -= 1
            left += 1
        while left > i:
            left -= 1
            cnt[info[arr[left]]] -= 1
            info[arr[left]] += 1
            cnt[info[arr[left]]] += 1
            if info[arr[left]] > max_cnt: max_cnt = info[arr[left]]
        answer[idx] = max_cnt

    print("\n".join(map(str, answer)))