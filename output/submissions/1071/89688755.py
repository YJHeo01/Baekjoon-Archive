from collections import deque

n = int(input())

cnt = [0] * 1001

array = sorted(list(map(int,input().split())))

for i in array: cnt[i] += 1

start = [True] * 1001

queue = deque([])

for i in range(1000):
    if cnt[i] != 0:
        start[i+1] = False
        queue.append(i)

if cnt[1000] != 0: queue.append(1000)

last = -2

answer = []

while queue:
    vx = queue.popleft()
    if last + 1 == vx:
        if queue == deque([]):
            for _ in range(cnt[last]):
                answer.pop()
            for _ in range(cnt[vx]):
                answer.append(vx)
            vx = last
        else:
            tmp = queue.popleft()
            queue.appendleft(vx)
            vx = tmp
    last = vx
    for _ in range(cnt[vx]):
        answer.append(vx)

print(*answer)