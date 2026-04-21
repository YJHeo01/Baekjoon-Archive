from collections import deque
import sys

input = sys.stdin.readline

def main():
    grow = list(map(int,input().split()))
    if k > 36:
        print("MEGA")
        return
    size = [[0]*(k+1) for _ in range(n+1)]
    bfs(grow,size)
    answer = max(size[n])
    if answer > 10 ** 11:
        print("MEGA")
    elif answer <= 0:
        print(-1)
    else:
        print(answer)

def bfs(grow,size):
    queue = deque([(0,0)])
    size[0][0] = s
    while queue:
        day, cnt = queue.popleft()
        if day == n: continue
        if size[day][cnt] + grow[day] > size[day+1][cnt]:
            size[day+1][cnt] = size[day][cnt] + grow[day]
            queue.append((day+1,cnt))
        if cnt == k: continue
        if size[day][cnt] * 2 > size[day+1][cnt+1]:
            size[day+1][cnt+1] = 2 * size[day][cnt]
            queue.append((day+1,cnt+1))
    
if __name__ == "__main__": 
    n,k,s = map(int,input().split())
    main()