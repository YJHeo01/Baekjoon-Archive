import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().split())))

def solution(graph,x1,y1,x2,y2):
    array = []
    if x1 + 1 == x2 and y1 + 1 == y2:
       for i in range(x1,x2+1):
           for j in range(y1,y2+1):
               array.append(graph[i][j])
    else:
        array.append(solution(graph,x1,y1,x2//2,y2//2))
        array.append(solution(graph,x2//2+1,y1,x2,y2//2))
        array.append(solution(graph,x1,y2//2+1,x2//2,y2))
        array.append(solution(graph,x2//2+1,y2//2+1,x2,y2))
    array.sort()
    return array[-2]

print(solution(matrix,0,0,n-1,n-1))