import sys

input = sys.stdin.readline

def main():
    graph = []
    r,c = map(int,input().split())
    for _ in range(r):
        graph.append(list(input()))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for x in range(r):
        for y in range(c):
            if graph[x][y] == 'W':
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
                    if graph[nx][ny] == 'S':
                        print(0)
                        return
    print(1)
    for x in range(r):
        for y in range(c):
            if graph[x][y] == '.': graph[x][y] = 'D'
            print(graph[x][y],end="")
        print()

if __name__ == "__main__":
    main()