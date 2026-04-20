import sys

input = sys.stdin.readline

n,p = map(int,input().split())

node = [list(map(int,input().split())) for _ in range(p)]
prefix_sum_R = [[0]*1001 for _ in range(1001)]
prefix_sum_L = [[0]*1001 for _ in range(1001)]

for i in range(p):
    left,right = i,(i+1) % p
    x1,y1 = node[left]
    x2,y2 = node[right]
    if x1 == x2:
        dy = 1
        if y1 > y2: dy = -1
        while True:
            if y1 == y2: break
            y1 += dy
            prefix_sum_R[x1][y1] = prefix_sum_R[x1][y1-dy] + 1
    else:
        dx = 1
        if x1 > x2: dx = -1
        while True:
            if x1 == x2: break
            x1 += dx
            prefix_sum_R[x1][y1] = prefix_sum_R[x1-dx][y1] + 1

for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    answer = abs(prefix_sum_R[x1][y1] - prefix_sum_R[x2][y2])
    tmp = min(prefix_sum_R[x1][y1],abs(prefix_sum_R[x1][y1] - prefix_sum_R[node[0][0]][node[0][1]])) + min(prefix_sum_R[x2][y2],abs(prefix_sum_R[x2][y2] - prefix_sum_R[node[0][0]][node[0][1]]))
    answer = min(answer,tmp)
    
    print(answer)
