from collections import deque
from itertools import permutations
import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    house = get_house()
    start = find_start(house)
    end = find_end(house)
    item = [start] + find_item(house) + [end]
    item_cnt = len(item)
    data = get_data(item_cnt)
    path_list = list(permutations(data,item_cnt-2))
    adj_matrix = get_adj_matrix(house,item)
    answer = get_answer(path_list,adj_matrix,item_cnt-1)
    print(answer)

def get_house():
    house = []
    for _ in range(n):
        house.append(list(input()))
    return house

def find_end(house):
    for x in range(n):
        for y in range(m):
            if house[x][y] == 'E': return (x,y)

def find_start(house):
    for x in range(n):
        for y in range(m):
            if house[x][y] == 'S': return (x,y)

def find_item(house):
    ret_value = []
    for x in range(n):
        for y in range(m):
            if house[x][y] == 'X': 
                ret_value.append((x,y))
    return ret_value

def get_data(item_cnt):
    data = []
    for i in range(1,item_cnt-1): data.append(i)
    return data

def get_adj_matrix(house,item):
    item_cnt = len(item)
    adj_matrix = [[INF]*item_cnt for _ in range(item_cnt)]
    for idx in range(item_cnt):
        start = item[idx]
        distance = [[INF]*m for _ in range(n)]
        bfs(house,distance,start)
        for i in range(item_cnt):
            x,y = item[i]
            adj_matrix[idx][i] = distance[x][y]
    return adj_matrix

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_house(nx,ny) or graph[nx][ny] == '#': continue
            if visited[nx][ny] <= visited[vx][vy] + 1: continue
            visited[nx][ny] = visited[vx][vy] + 1
            queue.append((nx,ny))
 
def exit_house(x,y):
    if x < 0 or y < 0 or x >= n or y >= m: return True
    return False

def get_sum_distance(path,adj_matrix):
    length = len(path); ret_value = 0
    for i in range(1,length):
        ret_value += adj_matrix[path[i]][path[i-1]]
    return ret_value

def get_answer(path_list,adj_matrix,last_idx):
    answer = INF
    for path in path_list:
        path = [0] + list(path) + [last_idx]
        answer = min(get_sum_distance(path,adj_matrix),answer)
    return answer

if __name__ == "__main__": 
    m,n = map(int,input().split())
    main()