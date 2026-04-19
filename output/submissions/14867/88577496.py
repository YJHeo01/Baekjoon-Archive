from collections import deque

a,b,c,d = map(int,input().split())

visited = dict([])
visited[(0,0)] = 0
queue = deque([(0,0)])
    
while queue:
    x,y = queue.popleft()

    sum_x_y = x + y
    
    if b > sum_x_y: a_to_b_x = 0; a_to_b_y = sum_x_y #Move water from x to y)
    else: a_to_b_x = sum_x_y - b; a_to_b_y = b
        
    if a > sum_x_y: b_to_a_x = sum_x_y; b_to_a_y = 0 #Move water from y to x)
    else: b_to_a_x = a; b_to_a_y = sum_x_y - a

    nx_ny_list = [(a,y),(0,y),(x,0),(x,b)] + [(b_to_a_x,b_to_a_y),(a_to_b_x,a_to_b_y)]
    
    for nx,ny in nx_ny_list:
        if (nx,ny) not in visited:
            visited[(nx,ny)] = visited[(x,y)] + 1
            queue.append((nx,ny))

target = (c,d)

if target in visited:
    print(visited[target])
else:
    print(-1)