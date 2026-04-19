import sys

sys.setrecursionlimit(10**6)

def main():
    array = list(map(int,input().split()))
    visited = [False] * n
    print(solution(array,visited))

def solution(array,visited):
    ret_value = 0
    for i in range(1,n-1):
        if visited[i] == True: continue
        visited[i] = True
        ret_value = max(ret_value,solution(array,visited)+array[get_L(visited,i)]*array[get_R(visited,i)])
        visited[i] = False
    return ret_value

def get_L(visited,x):
    while True:
        x -= 1
        if visited[x] == False:
            return x

def get_R(visited,x):
    while True:
        x += 1
        if visited[x] == False:
            return x

if __name__  == "__main__":
    n = int(input())
    main()