import sys, math

input = sys.stdin.readline

n,c = map(int,input().split())

arr = [0] + list(map(int,input().split()))

m = int(input())

answer = [0] * m

query = []

for idx in range(m):
    i,j = map(int,input().split())
    query.append((i,j,idx))

blk = int(math.sqrt(n))

query.sort(key=lambda x:(x[0]//blk,x[1] if (x[0] // blk) & 1 == 0 else -x[1]))

left,right = 1,0

rank = list(range(c+1)) #rank[색깔] -> 순위
info = list(range(c+1)) #info[순위] -> 색깔
cnt = [0] * (c+1)

for i,j,idx in query:
    while right < j:
        right += 1
        color = arr[right]
        target = 1 # 순위
        l,r = 1, rank[color]
        while l <= r:
            mid = (l+r) // 2
            if cnt[color] < cnt[info[mid]]:
                l = mid + 1
            else:
                target = mid
                r = mid - 1
        other_color = info[target]
        rank[color], rank[other_color],info[rank[color]], info[rank[other_color]] = rank[other_color], rank[color], info[rank[other_color]], info[rank[color]]
        cnt[color] += 1
    while right > j:
        color = arr[right]
        target = c # 순위
        l,r = rank[color], c
        while l <= r:
            mid = (l+r) // 2
            if cnt[color] == cnt[info[mid]]:
                target = mid
                l = mid + 1
            else :
                r = mid - 1
        other_color = info[target]
        rank[color], rank[other_color],info[rank[color]], info[rank[other_color]] = rank[other_color], rank[color], info[rank[other_color]], info[rank[color]]
        cnt[arr[right]] -= 1
        right -= 1
    while left < i:
        color = arr[left]
        target = c # 순위
        l,r = rank[color], c
        while l <= r:
            mid = (l+r) // 2
            if cnt[color] == cnt[info[mid]]:
                target = mid
                r = mid - 1
            else:
                l = mid + 1
        other_color = info[target]
        rank[color], rank[other_color],info[rank[color]], info[rank[other_color]] = rank[other_color], rank[color], info[rank[other_color]], info[rank[color]]
        cnt[arr[left]] -= 1
        left += 1
    while left > i:
        left -= 1
        color = arr[left]
        target = 1 # 순위
        l,r = 1, rank[color]
        while l <= r:
            mid = (l+r) // 2
            if cnt[color] < cnt[info[mid]]:
                l = mid + 1
            else:
                target = mid
                r = mid - 1
        other_color = info[target]
        rank[color], rank[other_color],info[rank[color]], info[rank[other_color]] = rank[other_color], rank[color], info[rank[other_color]], info[rank[color]]
        cnt[color] += 1
    if cnt[rank[1]] * 2 > (j-i+1): answer[idx] = rank[1]

for i in answer:
    if i == 0:
        print("no")
    else:
        print("yes"+" "+str(i))