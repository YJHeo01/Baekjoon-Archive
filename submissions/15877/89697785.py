import sys

input = sys.stdin.readline

def main():
    a,b = map(int,input().split())
    win = [[False]*1001 for _ in range(1001)]
    win[1][0], win[0][1] = True, True
    win[2][1], win[1][2] = True, True
    dx = [1,0,1,3]
    dy = [0,1,3,1]
    for x in range(3,1001):
        if x % 2 == 1: win[x][0], win[0][x] = True, True
        for y in range(1,x+1):
            for i in range(4):
                nx = x - dx[i]
                ny = y - dy[i]
                if nx < 0 or ny < 0: continue
                if win[nx][ny] == False: win[x][y] = True
                if win[ny][nx] == False: win[y][x] = True
    if win[a][b]:
        print("Alice")
    else:
        print("Bob")

if __name__ == "__main__":
    main()