from collections import deque
import math

def main():
    max_day = math.ceil(math.log2(n)+1)
    five_visited = [[] for _ in range(max_day+1)]
    six_visited = [[] for _ in range(max_day+1)]
    answer = -1
    get_visited_day(five_visited,a)
    get_visited_day(six_visited,b)
    for i in range(1,max_day+1):
        five_length = len(five_visited[i])
        six_length = len(six_visited[i])
        five_visited[i].sort(); six_visited[i].sort()
        five_idx, six_idx = 0,0
        while True:
            if five_idx == five_length or six_length == six_idx:
                break
            if five_visited[i][five_idx] > six_visited[i][six_idx]:
                six_idx += 1
            elif five_visited[i][five_idx] < six_visited[i][six_idx]:
                five_idx += 1
            else:
                answer = i
                break
        if answer != -1: break
    print(answer)

def get_visited_day(visited,start):
    queue = deque([(start,0)])
    visited[0].append(start)
    while queue:
        vx, day = queue.popleft()
        nx = vx + 2 ** day
        if nx <= n:
            visited[day+1].append(nx)
            queue.append((nx,day+1))
        nx = vx - 2 ** day
        if nx > 0:
            visited[day+1].append(nx)
            queue.append((nx,day+1))

if __name__ == "__main__":
    n,a,b = map(int,input().split())
    main()