def main():
    answer = int(1e9)
    a,b = map(int,input().split())
    graph = [list(input()) for _ in range(n)]
    for size in range(1,min(n,m)//3+1):
        for i in range(n-size*3+1):
            for j in range(m-size*3+1):
                answer = min(answer,get_cost(graph,a,b,(i,j),size))
                
    print(answer)

def get_cost(graph,a,b,start,size):
    ret_value = 0
    vx,vy = start
    dx = [1,1,1,0,0,0,2,2,2]
    dy = [1,2,0,0,1,2,0,1,2]
    for i in range(2):
        ret_value += b * change_tile_cnt(graph,'.',(vx+dx[i]*size,vy+dy[i]*size),size)
    for i in range(2,9):
        ret_value += a * change_tile_cnt(graph,'#',(vx+dx[i]*size,vy+dy[i]*size),size)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.': continue
            if i < vx or i >= vx + size * 3 or j < vy or j >= vy + size * 3: ret_value += b
    return ret_value

def change_tile_cnt(graph,target,start,size):
    ret_value = 0
    vx,vy = start
    for i in range(size):
        for j in range(size):
            if graph[vx+i][vy+j] != target: ret_value += 1
    return ret_value

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()