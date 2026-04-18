import math, sys

input = sys.stdin.readline

n,t = map(int,input().split())

arr = [0] + list(map(int,input().split()))

query = []

for i in range(t):
    l,r = map(int,input().split())
    query.append((l,r,i))

answer = [0] * t

blk = int(math.sqrt(n))

query.sort(query.sort(key=lambda x:(x[0]//blk,x[1] if (x[0] // blk) & 1 == 0 else -x[1])))

cnt = [0] * (int(1e6)+1)
left = 1
right = 0

power = 0

for i,j,idx in query:
    while right < j:
        right += 1
        power -= cnt[arr[right]] * cnt[arr[right]] * arr[right]
        cnt[arr[right]] += 1
        power += cnt[arr[right]] * cnt[arr[right]] * arr[right]
    while right > j:
        power -= cnt[arr[right]] * cnt[arr[right]] * arr[right]
        cnt[arr[right]] -= 1
        power += cnt[arr[right]] * cnt[arr[right]] * arr[right]
        right -= 1
    while left < i:
        power -= cnt[arr[left]] * cnt[arr[left]] * arr[left]
        cnt[arr[left]] -= 1
        power += cnt[arr[left]] * cnt[arr[left]] * arr[left]
        left += 1
    while left > i:
        left -= 1
        power -= cnt[arr[left]] * cnt[arr[left]] * arr[left]
        cnt[arr[left]] += 1
        power += cnt[arr[left]] * cnt[arr[left]] * arr[left]
    answer[idx] = power
    
for i in answer: print(i)