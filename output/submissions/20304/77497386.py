from collections import deque

INF = 21

def main():
    visited = [INF] * (n+1)
    password_list = list(map(int,input().split()))
    for password in password_list:
        visited[password] = 0
    answer = solution(visited,password_list)
    print(answer)

def solution(visited,start):
    queue = deque(start)
    ret_value = 0
    while queue:
        vx = queue.popleft()
        ret_value = visited[vx]
        for i in range(19,-1,-1):
            nx = vx & ((2**20-1) - 2**i)
            if nx > n:
                break
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
        for i in range(20):
            nx = vx | (2 ** i)
            if nx > n:
                break
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
    return ret_value

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    main()