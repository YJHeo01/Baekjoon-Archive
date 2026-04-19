import sys, heapq

input = sys.stdin.readline

#graph, dijkstra

def main():
    board = [list(input().rstrip()) for _ in range(n)]#회로
    distance = [[INF]*(m+1) for _ in range(n+1)]#각 꼭짓점에 도달하기 위한 최소 사용 전구 수
    dijk(board,distance)
    answer = distance[n][m]
    if answer >= INF:
        print("NO SOLUTION")
    else:
        print(answer)

def dijk(graph,distance):
    q = []
    heapq.heappush(q,(0,0,0))
    distance[0][0] = 0
    dx_dy = [(-1,-1),(1,1),(-1,1),(1,-1)] #좌측 두개는 /, 우측 두 개는 \일 경우 회로를 돌리지 않아도 됨
    use_for_board = [(-1,-1),(0,0),(-1,0),(0,-1)] #움직임 방향과 사용해야 하는 회로의 방향이 완전히 일치하지 않음으로, 이를 조정하기 위한 변수 리스트
    while q:
        dist, vx, vy = heapq.heappop(q)
        if dist > distance[vx][vy]: continue
        for move_type in range(4):
            dx,dy = dx_dy[move_type]
            nx = vx + dx
            ny = vy + dy
            if nx < 0 or ny < 0 or nx > n or ny > m: continue
            board_x, board_y = vx + use_for_board[move_type][0], vy + use_for_board[move_type][1]
            next_dist = dist
            if graph[board_x][board_y] == '/' and move_type < 2: next_dist += 1
            if graph[board_x][board_y] == '\\' and move_type >= 2: next_dist += 1
            if distance[nx][ny] > next_dist:
                distance[nx][ny] = next_dist
                heapq.heappush(q,(next_dist,nx,ny))

if __name__ == "__main__":
    INF = int(1e9)
    n,m = map(int,input().split())
    main()