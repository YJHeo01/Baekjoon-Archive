import sys, math

input = sys.stdin.readline

n,q = map(int,input().split())

arr = [0] + list(map(int,input().split()))

blk = int(math.sqrt(n))

querys = []

for i in range(q):
    a,b = map(int,input().split())
    querys.append((a,b,i))

answer = [0] * q

color = [0] * 100001

cnt = 0

querys.sort(key=lambda x:(x[0]//blk, x[1] if (x[0]//blk)%2==0 else -x[1]))

left = 1
right = 0

for x,y,i in querys:
    while left < x:
        color[arr[left]] -= 1
        if color[arr[left]] == 2: cnt -= 1
        left+=1
    while left > x:
        left -= 1
        color[arr[left]] += 1
        if color[arr[left]] == 3: cnt += 1
    while right > y:
        color[arr[right]] -= 1
        if color[arr[right]] == 2: cnt -= 1
        right -= 1
    while right < y:
        right += 1
        color[arr[right]] += 1
        if color[arr[right]] == 3: cnt += 1
    answer[i] = cnt

for i in answer:
    print(i)
        