import sys
from collections import deque

input = sys.stdin.readline

def main():
    while True:
        global w, h
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        block = [[False] * w for _ in range(h)]
        g = int(input())
        for _ in range(g):
            x, y = map(int, input().split())
            block[y][x] = True

        graph, adj = get_graph(block)

        time = [[INF] * w for _ in range(h)]
        time[0][0] = 0

        loop = bellman_ford(graph, adj, time)

        if loop:
            print("Never")
        elif time[h-1][w-1] >= INF:
            print("Impossible")
        else:
            print(time[h-1][w-1])

def get_graph(block):
    graph = []
    adj = [[] for _ in range(h*w)]

    def vid(y, x):
        return y*w + x

    hole = [[False] * w for _ in range(h)]
    e = int(input())
    for _ in range(e):
        x1, y1, x2, y2, t = map(int, input().split())
        hole[y1][x1] = True
        graph.append((y1, x1, y2, x2, t))
        adj[vid(y1, x1)].append(vid(y2, x2))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for y in range(h):
        for x in range(w):
            if block[y][x] or hole[y][x] or (y == h-1 and x == w-1):
                continue
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if ny < 0 or nx < 0 or ny >= h or nx >= w:
                    continue
                if block[ny][nx]:
                    continue
                graph.append((y, x, ny, nx, 1))
                adj[vid(y, x)].append(vid(ny, nx))

    return graph, adj

def bellman_ford(graph, adj, time):
    V = w * h

    for _ in range(V - 1):
        updated = False
        for y, x, ny, nx, t in graph:
            if time[y][x] == INF:
                continue
            cand = time[y][x] + t
            if time[ny][nx] > cand:
                time[ny][nx] = cand
                updated = True
        if not updated:
            break

    bad = [False] * V

    def vid(y, x):
        return y*w + x

    for y, x, ny, nx, t in graph:
        if time[y][x] == INF:
            continue
        if time[ny][nx] > time[y][x] + t:
            bad[vid(ny, nx)] = True
            bad[vid(y, x)] = True

    dq = deque([i for i, v in enumerate(bad) if v])
    inq = bad[:]

    while dq:
        v = dq.popleft()
        for nv in adj[v]:
            if not inq[nv]:
                inq[nv] = True
                dq.append(nv)

    if inq[vid(h-1, w-1)]:
        return True
    return False

if __name__ == "__main__":
    INF = int(1e18)
    main()