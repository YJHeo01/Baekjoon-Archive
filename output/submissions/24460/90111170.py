n = int(input())

array = [list(map(int,input().split())) for _ in range(n)]

def solution(x,y,size):
    if size == 1: return array[x][y]
    mid = size // 2
    tmp = sorted([solution(x,y,mid),solution(x,y+mid,mid),solution(x+mid,y,mid),solution(x+mid,y+mid,mid)])
    return tmp[1]

answer = solution(0,0,n)

print(answer)