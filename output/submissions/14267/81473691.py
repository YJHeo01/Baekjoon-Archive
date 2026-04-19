import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    array = [0] + list(map(int,input().split()))
    answer = [-1] * (n+1)
    point = [0] * (n+1)
    for _ in range(m):
        i,w = map(int,input().split())
        point[i] += w
    answer[1] = 0
    for i in range(2,n+1):
        answer[i] = solution(array,point,answer,i)
    print(*answer[1:])

def solution(graph,point,answer,vx):
    ret_value = point[vx]
    nx = graph[vx]
    if answer[nx] != -1:
        return ret_value + answer[nx]
    else:
        return ret_value + solution(graph,point,answer,nx)

if __name__ == "__main__":
    main()