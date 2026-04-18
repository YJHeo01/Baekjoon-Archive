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
        cnt[arr[right]] += 1
        color = arr[right]
        while True:
            if rank[color] == 1: break
            other_color = info[rank[color]-1]
            if cnt[color] <= cnt[other_color]: break
            info[rank[color]], info[rank[color]-1] = info[rank[color]-1], info[rank[color]]
            rank[color] -= 1
            rank[other_color] += 1
    while right > j:
        cnt[arr[right]] -= 1
        color = arr[right]
        while True:
            if rank[color] == c: break
            other_color = info[rank[color]+1]
            if cnt[color] >= cnt[other_color]: break
            info[rank[color]], info[rank[color]+1] = info[rank[color]+1], info[rank[color]]
            rank[color] += 1
            rank[other_color] -= 1
        right -= 1
    while left < i:
        cnt[arr[left]] -= 1
        color = arr[left]
        while True:
            if rank[color] == c: break
            other_color = info[rank[color]+1]
            if cnt[color] >= cnt[other_color]: break
            info[rank[color]], info[rank[color]+1] = info[rank[color]+1], info[rank[color]]
            rank[color] += 1
            rank[other_color] -= 1
        left += 1
    while left > i:
        left -= 1
        cnt[arr[left]] += 1
        color = arr[left]
        while True:
            if rank[color] == 1: break
            other_color = info[rank[color]-1]
            if cnt[color] <= cnt[other_color]: break
            info[rank[color]], info[rank[color]-1] = info[rank[color]-1], info[rank[color]]
            rank[color] -= 1
            rank[other_color] += 1
    if cnt[rank[1]] * 2 > (j-i+1): answer[idx] = rank[1]

for i in answer:
    if i == 0:
        print("no")
    else:
        print("yes"+" "+str(i))