from itertools import permutations
import sys, heapq

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
        node_list = get_node(k)
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
    ret_value = []
    for i in range(1,k+1): ret_value.append(i)
    return ret_value

def get_node(k):
    ret_value = [(0,0)]
    for _ in range(k):
        a, b = map(int,input().split())
        ret_value.append([a-1,b-1])
    return ret_value + [[m-1,n-1]]

def get_adj_matrix(graph,box_list):
    adj_matrix = [[[INF]*4 for _ in range(k+2)]for _ in range(k+2)]
    point_cnt = len(box_list)
    for start in range(point_cnt):
        for d in range(4):
            distance = [[INF]*n for _ in range(m)]
            x,y = box_list[start]
            bfs(graph,distance,(x,y,d))
            for end in range(point_cnt):
                end_x, end_y = box_list[end]
                adj_matrix[start][end][d] = distance[end_x][end_y] - d
    return adj_matrix

def bfs(graph,distance,start):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    x,y,k = start
    q = [];heapq.heappush(q,(k,x,y))
    distance[x][y] = k
    while q:
        vd,vx,vy = heapq.heappop(q)
        if vd > distance[vx][vy]: continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_graph(nx,ny): continue
            nd = get_nd(graph,distance,(vx,vy,i))
            if nd >= distance[nx][ny] : continue
            distance[nx][ny] = nd; heapq.heappush(q,(nd,nx,ny))

def exit_graph(x,y):
    if x < 0 or y < 0 or x >= m or y >= n: return True
    return False

def get_nd(graph,distance,point):
    direction = {'N':0,'E':1,'S':2,'W':3}
    x,y,d = point
    nd = distance[x][y]
    while True:
        if (nd + direction[graph[x][y]]) % 4 == d: return nd + 1
        nd += 1

def find_time(adj_matrix,test_case):
    ret_value = 0
    for i in range(1,k+2):
        cur = test_case[i-1]
        next = test_case[i]
        ret_value += adj_matrix[cur][next][ret_value%4]
    return ret_value

if __name__ == "__main__":
    main()