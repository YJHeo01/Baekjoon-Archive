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


cnt = [0] * (c+1)

for i,j,idx in query:
    while right < j:
        right += 1
        color = arr[right]
        cnt[color] += 1
    while right > j:
        color = arr[right]
        cnt[arr[right]] -= 1
        right -= 1
    while left < i:
        color = arr[left]
        cnt[arr[left]] -= 1
        left += 1
    while left > i:
        left -= 1
        color = arr[left]
        cnt[color] += 1
    for x in range(1,c+1):
        if cnt[x] * 2 > (j-i+1):
            answer[idx] = x
            break

for i in answer:
    if i == 0:
        print("no")
    else:
        print("yes"+" "+str(i))