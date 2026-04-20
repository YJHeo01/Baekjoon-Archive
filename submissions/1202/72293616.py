import sys,heapq

input = sys.stdin.readline

n,k = map(int,input().split())

jewel = []

for _ in range(n):
    m, v = map(int,input().split())
    heapq.heappush(jewel,(-v,m))

bag_empty = [True] * k
bag_list = []

for _ in range(k):
    bag_list.append(int(input()))
bag_list.sort()
INF = int(1e9)

def search_bag_idx(c,left,right):
    ret_value = INF
    while left <= right:
        mid = (left+right) // 2
        if bag_list[mid] >= c:
                ret_value = mid
                right = mid - 1
        else:
            left = mid + 1
    return ret_value

answer = 0
last_jewel_m = 0
last_jewel_idx = -1
while jewel != []:
    v,m = heapq.heappop(jewel)
    v *= -1
    if m >= last_jewel_m:
        idx = search_bag_idx(m,last_jewel_idx+1,k-1)
    else:
        idx = search_bag_idx(m,0,k-1)
    if idx == INF:
        continue
    while idx < k:
        if bag_empty[idx] == True:
            break
        idx += 1
    if idx < k:
        answer += v
        last_jewel_idx = idx
        last_jewel_m = m
        bag_empty[idx] = False

print(answer)