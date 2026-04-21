n,m,k = map(int,input().split())

arr = list(map(int,input().split()))

distance = 0

answer = ''

for start in range(k-1,-1,-1):
    left, right = 0, n+1
    while left <= right:
        mid = (left+right) // 2
        last = start
        tmp = '0' * start + '1'
        cnt = 1
        for i in range(start+1,k):
            if arr[i] - arr[last] >= mid:
                tmp += '1'
                cnt += 1
                last = i
            else:
                tmp += '0'
            if cnt == m: 
                tmp += '0' * (k-1-i)
                break
        if cnt >= m:
            if mid >= distance:
                answer = tmp
                distance = mid
            left = mid + 1 
        else:
            right = mid - 1

            
print(answer)