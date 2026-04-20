from itertools import permutations
from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    global m,n,k
    while True:
        m,n = map(int,input().split())
        if m == 0: break
        maze = get_maze(m)
        k = int(input())
        idx_list = get_idx_list(k)
        node_list = get_node_list(k)
        adj_matrix = get_adj_matrix(maze,node_list)
        test_case_list = list(permutations(idx_list,k))
        answer = INF
        for test_case in test_case_list:
            test_case = [0] + list(test_case) + [k+1]
            answer = min(answer,find_time(adj_matrix,test_case))
        print(answer)

def get_maze(m):
    maze = []
    for _ in range(m): maze.append(list(input()))
    return maze

def get_idx_list(k):
    idx_list = []
    for i in range(1,k+1): idx_list.append(i)
    return idx_list

def get_node_list(k):
    ret_value = [(0,0)]
    for _ in range(k):
        a, b = map(int,input().split())
        ret_value.append([a-1,b-1])
    return ret_value + [[m-1,n-1]]

def get_adj_matrix(graph,node_list):
    adj_matrix = [[[INF]*4 for _ in range(k+2)]for _ in range(k+2)]
    point_cnt = len(node_list)
    for start in range(point_cnt):
        for d in range(4):
            distance = [[INF]*n for _ in range(m)]
            x,y = node_list[start]
            bfs(graph,distance,(x,y,d))
            for end in range(point_cnt):
                end_x, end_y = node_list[end]
                adj_matrix[start][end][d] = distance[end_x][end_y] - d
    return adj_matrix

def bfs(graph,distance,start):
    visited = [[INF]*n for _ in range(m)]
    direction = {'N':0,'E':1,'S':2,'W':3}
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    x,y,k = start
    queue = deque([(x,y)])
    distance[x][y] = k; visited[x][y] = k
    while queue:
        vx,vy = queue.popleft()
        wait = False
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_graph(nx,ny) or visited[vx][vy] + 1 >= distance[nx][ny]: continue
            if (visited[vx][vy] + direction[graph[vx][vy]]) % 4 != i : wait = True; continue
            distance[nx][ny] = visited[vx][vy] + 1; visited[nx][ny] = distance[nx][ny]
            queue.append((nx,ny))
        if wait == True: visited[vx][vy] += 1; queue.append((vx,vy))
    
def exit_graph(x,y):
    if x < 0 or y < 0 or x >= m or y >= n: return True
    return False

def find_time(adj_matrix,test_case):
    ret_value = 0
    for i in range(1,k+2):
        cur = test_case[i-1]
        next = test_case[i]
        ret_value += adj_matrix[cur][next][ret_value%4]
    return ret_value

if __name__ == "__main__":
    main()