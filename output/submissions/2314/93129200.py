from collections import deque

start = ""

for _ in range(4):
    start += input()

queue = deque([start])

visited = dict()

visited[start] = 0

dx = [4,-4,1,-1]

while queue:
    cur_state = queue.popleft()
    for i in range(16):
        for j in range(4):
            if i % 4 == 3 and j == 2: continue
            if i % 4 == 0 and j == 3: continue
            if i // 4 == 0 and j == 1: continue
            if i // 4 == 3 and j == 0: continue
            tmp = list(cur_state)
            tmp[i], tmp[(i+dx[j])%16] = tmp[(i+dx[j])%16], tmp[i]
            next_state = ""
            for k in range(16):
                next_state += tmp[k]
            if next_state not in visited:
                visited[next_state] = visited[cur_state] + 1
                queue.append(next_state)

end = ""

cnt = 4

while cnt:
    tmp = input()
    if tmp != "":
        cnt -= 1
        end += tmp

print(visited[end])