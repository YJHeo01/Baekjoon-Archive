import sys

input = sys.stdin.readline

def main():
    visited = [[False]*m for _ in range(n)]
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    print(backtraking(graph,visited,0,0))

def backtraking(graph,visited,idx,value):
    if idx == n * m:
        return value
    x,y = idx // m, idx % m
    ret_value = backtraking(graph,visited,idx+1,value)
    if visited[x][y] == True: return ret_value
    item_list = [[(0,1),(1,0)],[(0,-1),(-1,0)],[(0,-1),(1,0)],[(0,1),(-1,0)]]
    visited[x][y] = True
    for item in item_list:
        if check_append_weapon(item,visited,(x,y))== False: continue
        ret_value = max(ret_value,backtraking(graph,visited,idx+1,append_weapon(graph,visited,item,(x,y),value)))
        remove_weapon(item,visited,(x,y))
    visited[x][y] = False
    return ret_value

def check_append_weapon(item,visited,point):
    x,y = point
    for dx,dy in item:
        nx = x + dx; ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] == True:
            return False
    return True

def append_weapon(graph,visited,item,point,value):
    x,y = point
    next_value = value + 2 * graph[x][y]
    for dx,dy in item:
        nx = x + dx
        ny = y + dy
        visited[nx][ny] = True
        next_value += graph[nx][ny]
    return next_value

def remove_weapon(item,visited,point):
    x,y = point
    for dx,dy in item:
        visited[x+dx][y+dy] = False

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()