import sys, math

input = sys.stdin.readline

n,q = map(int,input().split())

arr = [0] + list(map(int,input().split()))

tmp = set(arr[1:])

tmp = sorted(list(tmp))

convert = dict()

l = len(tmp)

for i in range(l):
  convert[tmp[i]] = i

for i in range(n):
  arr[i+1] = convert[arr[i+1]]

answer = [0] * q

query = []

for idx in range(q):
    i,j = map(int,input().split())
    query.append((i,j,idx))

blk = int(math.sqrt(n))

query.sort(key=lambda x:(x[0]//blk,x[1] if (x[0] // blk) & 1 == 0 else -x[1]))

left,right = 1,0

state = [0] * (n+1)

cnt = 0

for i,j,idx in query:
    while right < j:
        right += 1
        if state[arr[right]] == 2:
            cnt -= 1
        state[arr[right]] += 1
        if state[arr[right]] == 2: cnt+=1
    while right > j:
        if state[arr[right]] == 2:
            cnt -= 1
        state[arr[right]] -= 1
        if state[arr[right]] == 2:
            cnt += 1
        right -= 1
    while left < i:
        if state[arr[left]] == 2:
            cnt -= 1
        state[arr[left]] -= 1
        if state[arr[left]] == 2:
            cnt += 1
        left += 1
    while left > i:
        left -= 1
        if state[arr[left]] == 2:
            cnt -= 1
        state[arr[left]] += 1
        if state[arr[left]] == 2:
            cnt += 1
    answer[idx] = cnt

for i in answer:
    print(i)