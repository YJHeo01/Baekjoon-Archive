from collections import deque

n,m = map(int,input().split())

target = list(map(int,input().split()))

queue = deque(range(1,n+1))

answer = 0

for i in target:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            l = len(queue)
            left_cnt = 0
            right_cnt = 0
            for k in range(l):
                if queue[k] == i:
                    break
                left_cnt += 1
            for k in range(l-1,-1,-1):
                right_cnt += 1
                if queue[k] == i: break
            if left_cnt < right_cnt:
                queue.append(queue.popleft())
            else:
                queue.appendleft(queue.pop())
            answer += 1
        
print(answer)