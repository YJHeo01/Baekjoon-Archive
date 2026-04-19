from collections import deque
import sys

input = sys.stdin.readline

def main():
    point_list = [(0,0)]
    y_point = [[] for _ in range(t+1)]
    y_point[0].append(0)
    for i in range(1,n+1):
        x,y = map(int,input().split())
        y_point[y].append(i)
        point_list.append((x,y))
    visited = [-1] * (n+1)
    bfs(point_list,y_point,visited)
    answer = 50001
    for target_idx in y_point[t]:
        if visited[target_idx] == -1:continue
        answer = min(answer,visited[target_idx])
    if answer == 50001:answer = -1
    print(answer)

def bfs(point_list,y_point,visited):
    queue = deque([0])
    visited[0] = 0
    while queue:
        cur_idx = queue.popleft()
        vx,vy = point_list[cur_idx]
        for dy in range(-2,3):
            ny = vy + dy
            if ny < 0 or ny > t: continue
            for next_idx in y_point[ny]:
                if visited[next_idx] != -1: continue
                if abs(point_list[next_idx][0] - vx) > 2: continue
                visited[next_idx] = visited[cur_idx] + 1
                queue.append(next_idx)

if __name__ == "__main__":
    n,t = map(int,input().split())
    main()