def main():
    while True:
        a,b = input().split()
        if a == '0': break
        visited_a = [INF] * 1000; visited_b = [INF] * 1000
        if int(a) < 1000: visited_a[int(a)] = 1
        if int(b) < 1000: visited_b[int(b)] = 1
        start_a = get_nx(a); start_b = get_nx(b)
        visited_a[start_a] = min(visited_a[start_a],2); visited_b[start_b] = min(2,visited_b[start_b])
        dfs(visited_a,start_a); dfs(visited_b,start_b)
        length = INF
        for i in range(1000):
            length = min(length,visited_a[i]+visited_b[i])
        if length >= INF: length = 0
        print(a,b,length)

def dfs(visited,vx):
    nx = get_nx(str(vx))
    if visited[nx] == INF:
        visited[nx] = visited[vx] + 1
        dfs(visited,nx)

def get_nx(vx):
    stack = list(vx)
    nx = 0
    while stack:
        nx += (int(stack.pop())) ** 2
    return nx

if __name__ == "__main__":
    INF = int(1e9)
    main()
