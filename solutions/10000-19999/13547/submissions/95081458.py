import sys, math

input = sys.stdin.readline

n = int(input())

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

state = [0] * 1000001

cnt = 0

for i,j,idx in query:
    while right < j:
        right += 1
        if state[arr[right]] == 0:
            cnt += 1
        state[arr[right]] += 1
    while right > j:
        state[arr[right]] -= 1
        if state[arr[right]] == 0:
            cnt -= 1
        right -= 1
    while left < i:
        state[arr[left]] -= 1
        if state[arr[left]] == 0:
            cnt -= 1
        left += 1
    while left > i:
        left -= 1
        if state[arr[left]] == 0:
            cnt -= 1
        state[arr[left]] += 1
    answer[idx] = cnt

for i in answer:
    print(i)