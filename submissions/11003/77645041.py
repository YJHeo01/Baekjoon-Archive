from collections import deque

INF = int(1e9)

n,l = map(int,input().split())

array = list(map(int,input().split()))

queue = deque([])

min_value = INF

for i in range(l):
    queue.append(array[i])
    if min_value > array[i]:
        min_value = array[i]
    print(min_value,end=" ")

for i in range(l,n):
    queue.append(array[i])
    remove_value = queue.popleft()
    if array[i] > min_value:
        if remove_value == min_value:
            min_value = min(queue)
    else:
        min_value = array[i]
    print(min_value,end=" ")