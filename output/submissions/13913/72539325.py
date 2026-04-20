from collections import deque

n,k = map(int,input().split())

length = 100001
INF = int(1e9)
dp = [INF] * length

def bfs(visited,start):
    queue = deque([start])
    visited[start] = 0
    dx = [1,-1]
    while queue:
        vx = queue.popleft()
        for i in range(2):
            nx = vx + dx[i]
            if nx < 0 or nx >= length:
                continue
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
        if vx * 2 < length:
            if visited[vx*2] > visited[vx] + 1:
                visited[vx*2] = visited[vx] + 1
                queue.append(vx*2)

bfs(dp,n)

def print_second_line_answer(array):
    while True:
        if array == []:
            return
        print(array.pop(),end=" ")

def get_second_line_answer(visited,position):
    second_line = []
    while True:
        second_line.append(position)
        if visited[position] == 0:
            return second_line
        if visited[position] == visited[position-1] + 1:
            next_position = position - 1
        elif visited[position] == visited[position+1] + 1:
            next_position = position + 1
        else:
            next_position = position // 2
        position = next_position

print(dp[k])
second_line_answer = get_second_line_answer(dp,k)
print_second_line_answer(second_line_answer)