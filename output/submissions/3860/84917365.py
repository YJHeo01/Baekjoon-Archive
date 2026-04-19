import sys

input = sys.stdin.readline

def main():
    while True:
        global w,h
        w,h = map(int,input().split())
        if w == 0 and h == 0: break
        block = [[False]*w for _ in range(h)]
        g = int(input())
        for _ in range(g):
            x,y = map(int,input().split())
            block[y][x] = True
        graph = get_graph(block)
        time = [[INF]*w for _ in range(h)]
        time[0][0] = 0
        answer = bellman_ford(graph,time)
        if answer >= INF:
            print("Impossible")
        elif answer < 0:
            print("Never")
        else:
            print(answer)

def get_graph(block):
    graph = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for vx in range(h):
        for vy in range(w):
            if block[vx][vy]: continue
            for k in range(4):
                nx = vx + dx[k]
                ny = vy + dy[k]
                if nx < 0 or ny < 0 or nx >= h or ny >= w or block[nx][ny]: continue
                graph.append((vx,vy,nx,ny,1))
    e = int(input())
    for _ in range(e):
        x1,y1,x2,y2,t = map(int,input().split())
        graph.append((y1,x1,y2,x2,t))
    return graph

def bellman_ford(graph,time):
    for _ in range(w*h):
        for vx,vy,nx,ny,t in graph:
            if time[nx][ny] > time[vx][vy] + t:
                time[nx][ny] = time[vx][vy] + t
    for vx,vy,nx,ny,t in graph:
        if time[nx][ny] > time[vx][vy] + t:
            return -1
    return time[h-1][w-1]

if __name__ == "__main__":
    INF = int(1e11)
    main()