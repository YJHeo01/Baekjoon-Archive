from collections import deque
n,a,b = map(int,input().split())
cur_queue = deque([])
for i in range(1,n+1):
    cur_queue.append(i)
answer = 1
while True:
    next_queue= deque([])
    while cur_queue:
        left = cur_queue.popleft()
        if cur_queue == deque([]):
            next_queue.append(left)
            break
        right = cur_queue.popleft()
        if (left == a and right == b) or (left == b and right == a):
            print(answer)
            exit(0)
        if right == b or right == a:
            next_queue.append(right)
        else:
            next_queue.append(left)
    answer += 1
    cur_queue = next_queue