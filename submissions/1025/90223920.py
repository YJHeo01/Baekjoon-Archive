import math

n,m = map(int,input().split())

array = [list(input()) for _ in range(n)]

answer = -1

def check(value):
    tmp = int(math.sqrt(value))
    arr = [(tmp-1)**2,tmp**2,(tmp+1)**2]
    for i in arr:
        if i == value: return True
    return False

for i in range(n):
    for j in range(m):
        for dx in range(-i,n-i):
            for dy in range(-j,m-j):
                x,y = i,j
                tmp = int(array[i][j])
                if tmp == 0:
                    answer = max(answer,0)
                    continue
                while True:
                    if tmp > answer and check(tmp):
                        answer = tmp
                    if dx == 0 and dy == 0: break
                    x += dx; y += dy
                    if x >= n or y >= m or x < 0 or y < 0: break
                    tmp *= 10
                    tmp += int(array[x][y])
                    
print(answer)