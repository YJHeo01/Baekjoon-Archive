import sys, heapq

input = sys.stdin.readline

def main():
    board = [list(input().rstrip()) for _ in range(n)]
    distance = [[INF]*(m+1) for _ in range(n+1)]
    dijk(board,distance)
    answer = distance[n][m]
    print(answer)
def dijk(graph,distance):
    q = []
    heapq.heappush(q,(0,0,0))
    distance[0][0] = 0
    dx_dy = [(-1,-1),(1,1),(-1,1),(1,-1)]
    use_board = [(-1,-1),(0,0),(-1,0),(0,-1)]
    while q:
        dist, vx, vy = heapq.heappop(q)
        if dist > distance[vx][vy]: continue
        for move_type in range(2):
            dx,dy = dx_dy[move_type]
            nx = vx + dx
            ny = vy + dy
            if nx < 0 or ny < 0 or nx > n or ny > m: continue
            board_x, board_y = vx + use_board[move_type][0], vy + use_board[move_type][1]
            next_dist = dist
            if graph[board_x][board_y] == '/': next_dist += 1
            if distance[nx][ny] > next_dist:
                distance[nx][ny] = next_dist
                heapq.heappush(q,(next_dist,nx,ny))
        for move_type in range(2,4):
            dx,dy = dx_dy[move_type]
            nx = vx + dx
            ny = vy + dy
            if nx < 0 or ny < 0 or nx > n or ny > m: continue
            board_x, board_y = vx + use_board[move_type][0], vy + use_board[move_type][1]
            next_dist = dist
            if graph[board_x][board_y] == '\\': next_dist += 1
            if distance[nx][ny] > next_dist:
                distance[nx][ny] = next_dist
                heapq.heappush(q,(next_dist,nx,ny))

if __name__ == "__main__":
    INF = int(1e9)
    n,m = map(int,input().split())
    main()
