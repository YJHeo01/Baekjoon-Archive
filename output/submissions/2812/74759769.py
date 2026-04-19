from collections import deque

n,k = map(int,input().split())

queue = deque(list(input()))

stack = []
stack.append(queue.popleft())

erase_cnt = 0

left = int(stack.pop())
right = int(queue.popleft())
while True:
    if left >= right:
        stack.append(left)
        left = right
        if queue == deque([]):
            stack.append(left)
            break   
        right = int(queue.popleft())              
    elif stack == []:
        erase_cnt += 1
        left = right
        if queue == deque([]):
            stack.append(left)
            break
        right = int(queue.popleft())
    else:
        erase_cnt += 1
        left = stack.pop()

    if erase_cnt == k:
        stack.append(left)
        stack.append(right)
        break
    
stack += list(queue)

length = n-k

for i in range(length):
    print(stack[i],end="")