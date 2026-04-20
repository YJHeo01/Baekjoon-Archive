from collections import deque

a,b,c,d = map(int,input().split())

def bfs(visited):
    visited[(0,0)] = 0
    queue = deque([(0,0)])
    
    while queue:
        x,y = queue.popleft()

        sum_x_y = x + y
        
        if a > sum_x_y:
            b_to_a_x = sum_x_y
            b_to_a_y = 0
        else:
            b_to_a_x = a
            b_to_a_y = sum_x_y - a
            
        if b > sum_x_y:
            a_to_b_x = 0
            a_to_b_y = sum_x_y
        else:
            a_to_b_x = sum_x_y - b
            a_to_b_y = b
        
        nx_ny_list = [(a,y),(0,y),(x,0),(x,b)] + [(b_to_a_x,b_to_a_y),(a_to_b_x,a_to_b_y)]
    
        for nx,ny in nx_ny_list:
            if (nx,ny) not in visited:
                visited[(nx,ny)] = visited[(x,y)] + 1
                queue.append((nx,ny))

visited = dict([])

bfs(visited)

target = (c,d)

if target in visited:
    print(visited[target])
else:
    print(-1)