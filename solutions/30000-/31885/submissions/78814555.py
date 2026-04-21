import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,k = map(int,input().split())

item = []

for _ in range(n):
    item.append(list(map(int,input().split())))

end_x, end_y = map(int,input().split())

def solution(item,start,hp):
    x,y = start
    if x == end_x and y == end_y:
        return hp
    if hp == 0: return -1
    ret_value = -1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        ret_value = max(ret_value,solution(item,(nx,ny),hp-1))
    if hp >= 2:
        for dx,dy in item:
            nx = x + dx
            ny = y + dy
            ret_value = max(ret_value,solution(item,(nx,ny),hp-2))
    return ret_value

answer = k - solution(item,(0,0),k)

if answer > k:
    answer = -1

print(answer)