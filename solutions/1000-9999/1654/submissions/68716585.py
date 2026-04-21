k, n = map(int,input().split())

lan = []

min_v = 0
max_v = 0
for i in range(k):
    tmp = int(input())
    if tmp > max_v:
        max_v = tmp
    lan.append(tmp)

def binary_search(low,high):
    answer = 0    
    while(low<=high):
        mid = (low+high)//2
        cnt = 0
        for i in lan:
            cnt += (i//mid)
        if cnt >= n:
            answer = max(answer,mid)
            low = mid + 1
        else:
            high = mid - 1
    print(answer)

binary_search(min_v,max_v)