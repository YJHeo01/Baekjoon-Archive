from collections import deque
import sys

input = sys.stdin.readline

def main():
    INF = int(1e9)
    init_array = list(input().split())
    visited = {}
    bfs(init_array,visited,k)
    answer = INF
    for array in visited:
        correct_array = True
        for i in range(1,n):
            if int(array[i]) < int(array[i-1]):
                correct_array = False
                break
        if correct_array == True:
            answer = min(answer,visited[array])
    if answer >= INF:
        answer = -1
    print(answer)

def bfs(array,visited,k):
    start = ""
    for i in array:
        start += i
    visited[start] = 0
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        for i in range(n-k+1):
            nx = vx[:i]
            for j in range(k-1,-1,-1):
                nx += vx[i+j]
            nx += vx[i+k:]
            if nx not in visited:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

if __name__ == "__main__":
    n,k = map(int,input().split())
    main()