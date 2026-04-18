from collections import deque

A = input()
B = input()

length = len(A)

visited = dict()

visited[A] = 0

queue = deque([A])

while queue:
    s = queue.popleft()
    for i in range(length):
        for j in range(i+1):
            tmp = s[:j]+ s[j:i+1][::-1] + s[i+1:]
            if tmp not in visited:
                visited[tmp] = visited[s] + 1
                queue.append(tmp)

if B not in visited:
    print(-1)
else:
    print(visited[B])