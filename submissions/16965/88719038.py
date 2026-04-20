from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    set_list = []
    for _ in range(n):
        c,x,y = map(int,input().split())
        
        if c == 1: set_list.append((x,y)); continue
        
        visited = [False] * len(set_list)
        bfs(set_list,visited,x-1)
        
        print(int(visited[y-1]))
            
def bfs(set_list,visited,start):
    queue = deque([start])
    visited[start] = True
    set_cnt = len(visited)
    while queue:
        cur_node = queue.popleft()
        for next_node in range(set_cnt):
            if visited[next_node]: continue
            x1,y1 = set_list[cur_node]
            x2,y2 = set_list[next_node]
            if (x2<x1<y2) or (x2<y1<y2):
                visited[next_node] = True
                queue.append(next_node)
                
if __name__ == "__main__":
    main()