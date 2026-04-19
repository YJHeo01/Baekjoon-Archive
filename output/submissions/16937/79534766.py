import sys

input = sys.stdin.readline

def main():
    h,w = map(int,input().split())
    n = int(input())
    sticker = []
    for _ in range(n):
        sticker.append(list(map(int,input().split())))
    answer = 0
    for a in range(1,n):
        for b in range(a):
            x1 = [sticker[a][0],sticker[a][1],sticker[a][1],sticker[a][0]]
            y1 = [sticker[a][1],sticker[a][0],sticker[a][0],sticker[a][1]]
            x_a = [sticker[a][0],sticker[a][1],0,0]
            y_a = [0,0,sticker[a][0],sticker[a][1]]
            dx = [sticker[b][0],sticker[b][1]]
            dy = [sticker[b][1],sticker[b][0]]
            size = sticker[a][0] * sticker[a][1] + sticker[b][0]*sticker[b][1]
            if answer >= size:continue
            for i in range(4):
                vx = x_a[i]
                vy = y_a[i]
                if x1[i] > h or y1[i] > w:continue
                for k in range(2):
                    nx = vx + dx[k]
                    ny = vy + dy[k]
                    if nx > h or ny > w:continue
                    answer = size
                    break
    print(answer)