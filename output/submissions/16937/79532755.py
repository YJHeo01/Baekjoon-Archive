import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    sticker = []
    for _ in range(n):
        a,b = map(int,input().split())
        sticker.append((a,b))
    area = [[False]*w for _ in range(h)]
    use_sticker = [False] * n
    answer = solution(sticker,area,use_sticker,(0,0),0)
    print(answer)

def solution(sticker,area,use_sticker,point,cnt):
    ret_value = 0
    vx,vy = point
    if vy == w: vx,vy = vx + 1,0
    if cnt == 2 or vx == h: return 0
    if area[vx][vy] == True:
        return solution(sticker,area,(vx,vy+1),cnt)
    for i in range(n):
        if use_sticker[i] == True:continue
        use_sticker[i] = True
        dx = [sticker[i][0],sticker[i][1]]
        dy = [sticker[i][1],sticker[i][0]]
        size = dx[0] * dy[0]
        for j in range(2):
            nx = vx + dx[j]
            ny = vy + dy[j]
            if nx > h or ny > w:continue
            set_area(area,vx,vy,nx,ny,True)
            new_size = solution(sticker,area,use_sticker,(vx,ny),cnt+1)
            if cnt == 1 or new_size != 0: new_size += size
            ret_value = max(ret_value,new_size)
            set_area(area,vx,vy,nx,ny,False)
        use_sticker[i] = False    
    return ret_value

def set_area(area,x1,y1,x2,y2,value):
    for x in range(x1,x2):
        for y in range(y1,y2):
            area[x][y] = value
    return area

if __name__ == "__main__":
    h,w = map(int,input().split())
    n = int(input())
    main()