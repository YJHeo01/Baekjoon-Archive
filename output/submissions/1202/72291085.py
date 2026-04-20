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
max_bag = bag_list[-1]
INF = int(1e9)

def search_bag_idx(c):
    ret_value = INF
    left, right = 0,k-1
    while left <= right:
        mid = (left+right) // 2
        if bag_list[mid] >= c:
                ret_value = mid
                right = mid - 1
        else:
            left = mid + 1
    return ret_value

answer = 0

while jewel != []:
    v,m = heapq.heappop(jewel)
    if m > max_bag:
        continue
    v *= -1
    idx = search_bag_idx(m)
    if idx == INF:
        continue
    if bag_empty[idx] == False:
        while idx < k:
            if bag_empty[idx] == True:
                break
            idx += 1
    if idx < k:
        answer += v
        bag_empty[idx] = False

print(answer)