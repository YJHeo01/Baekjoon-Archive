import sys

input = sys.stdin.readline

m,n = map(int,input().split())
edge_bug_list = [1] * (2*m-1)

def edge_bug_grow(bug_list,two,one):
    idx = 0
    while True:
        if two == 0:
            break
        two -= 1
        bug_list[idx] += 2
        idx += 1
    while True:
        if one == 0:
            break
        one -= 1
        bug_list[idx] += 1
        idx += 1
    return

def grow_two(column_grow_value,start_y):
    for y in range(start_y,m):
        column_grow_value[y] += 2

def grow_one(column_grow_value,one_start_y,two_start_y):
    for y in range(one_start_y,two_start_y):
        column_grow_value[y] += 1

def get_start_y(last_start_y,value):
    ret_value = last_start_y - value
    if ret_value <= 0:
        ret_value = 1
    return ret_value

column_grow_value = [1] * m

for _ in range(n):
    zero, one, two = map(int,input().split())
    edge_bug_grow(edge_bug_list,two,one)
    if two != 0:
        if two >= m-1:
            grow_two(column_grow_value,1)
            continue
        two_start_y = get_start_y(m,two)
        grow_two(column_grow_value,two_start_y)
        if one == 0:
            continue
        one_start_y = get_start_y(two_start_y,one)
        grow_one(column_grow_value,one_start_y,two_start_y)
    elif one != 0:
        one_start_y = get_start_y(m,one)
        grow_one(column_grow_value,one_start_y,m)
    else:
        continue

def print_north_edge(north_edge):
    for i in range(m):
        print(north_edge[i],end=" ")
    print()

west_edge = edge_bug_list[m:]
north_edge = edge_bug_list[:m]
north_edge.reverse()
print_north_edge(north_edge)

for i in range(m-1):
    print(west_edge[i],end=" ")
    for j in range(1,m):
        print(column_grow_value[j],end=" ")
    print()