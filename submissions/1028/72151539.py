import sys
input = sys.stdin.readline

r,c = map(int,input().split())

mine = []

for _ in range(r):
    mine.append(list(input()))


max_size = ((min(r,c)+1)//2)

def check_diamond(graph,size,start):
    x, y = start
    for i in range(size):
        dx = [i,-i,-i,i]
        dy = [(size-i-1),-(size-i-1),(size-i-1),-(size-i-1)]
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if graph[nx][ny] == '0':
                return False
    return True

def solution():
    for k in range(max_size,0,-1):
        for i in range(k-1,r-k+1):
            for j in range(k-1,c-k+1):
                if check_diamond(mine,k,(i,j)) == True:
                    return k
    
    return 0

answer = solution()

print(answer)
