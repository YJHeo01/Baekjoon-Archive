import sys

input = sys.stdin.readline

m,n = map(int,input().split())

size = [[1]*m for _ in range(m)]
north_west_edge_bug_list = []

for i in range(m-1,0,-1):
    north_west_edge_bug_list.append((0,i))

for i in range(m):
    north_west_edge_bug_list.append((i,0))

def north_west_edge_bug_grow(size,bug_list,two,one):
    idx = 0
    while True:
        if two == 0:
            break
        two -= 1
        x,y = bug_list[idx]
        size[x][y] += 2
        idx += 1
    while True:
        if one == 0:
            break
        one -= 1
        x,y = bug_list[idx]
        size[x][y] += 1
        idx += 1
    return

def grow_two(size,start_y):
    for x in range(1,m):
        for y in range(start_y,m):
            size[x][y] += 2

def grow_one(size,one_start_y,two_start_y):
    for x in range(1,m):
        for y in range(one_start_y,two_start_y):
            size[x][y] += 1

def get_start_y(last_start_y,value):
    ret_value = last_start_y - value
    if ret_value <= 0:
        ret_value = 1
    return ret_value

for _ in range(n):
    zero, one, two = map(int,input().split())
    north_west_edge_bug_grow(size,north_west_edge_bug_list,two,one)
    if two != 0:
        if two >= m-1:
            grow_two(size,1)
            continue
        two_start_y = get_start_y(m,two)
        grow_two(size,two_start_y)
        if one == 0:
            continue
        one_start_y = get_start_y(two_start_y,one)
        grow_one(size,one_start_y,two_start_y)
    elif one != 0:
        one_start_y = get_start_y(n,one)
        grow_one(size,one_start_y,m)
    else:
        continue

for i in range(m):
    for j in range(m):
        print(size[i][j],end=" ")
    print()