import sys

input = sys.stdin.readline

def main():
    parent = [0] * k
    area = [[]for _ in range(k)]
    world = [[-1]*n for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        x -= 1; y -= 1
        area[i].append((x,y))
        world[x][y] = i
        parent[i] = i
    answer = solution(world,parent,area)
    print(answer)

def solution(world,parent,area):
    time = 0
    while True:
        check_adj_area(world,parent,area)
        if check_finish(parent) == True: return time
        time += 1
        for i in range(k):
            area[i] = get_new_area(world,parent,area[i])

def check_adj_area(world,parent,area):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for cur_idx in range(k):
        for x,y in area[cur_idx]:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >=n:continue
                adj_idx = world[nx][ny]
                if adj_idx == -1 or adj_idx == cur_idx: continue
                union_parent(parent,cur_idx,adj_idx)
                
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check_finish(parent):
    for i in range(k):
        if find_parent(parent,i) != 0: return False
    return True

def get_new_area(world,parent,area):
    new_area = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while area:
        vx,vy = area.pop()
        cur_idx = world[vx][vy]
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or world[nx][ny] == cur_idx:
                continue
            adj_idx = world[nx][ny]
            if adj_idx == -1:
                world[nx][ny] = cur_idx
                new_area.append((nx,ny))
            else:
                union_parent(parent,cur_idx,adj_idx)
    return new_area

if __name__ == "__main__":
    n,k = map(int,input().split())
    main()