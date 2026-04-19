import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())
array_A = []
ground = [[5]*n for _ in range(n)]
for _ in range(n):
    array_A.append(list(map(int,input().split())))
        
tree_list = []

for _ in range(m):
    x,y,z = map(int,input().split())
    tree_list.append([z,x-1,y-1])

def spring(ground,tree_list):
    dead_tree = []
    live_tree = []
    for tree in tree_list:
        age, x, y = tree
        if ground[x][y] >= age:
            ground[x][y] -= age
            live_tree.append([age+1,x,y])
        else:
            dead_tree.append([age,x,y])
    return live_tree, dead_tree

def summer(ground,dead_tree):
    for tree in dead_tree:
        age,x,y = tree
        ground[x][y] += (age // 2)

def autumn(tree_list):
    dx = [1,1,1,0,0,-1,-1,-1]
    dy = [-1,0,1,-1,1,-1,0,1]
    new_tree_list = []
    for tree in tree_list:
        age,x,y = tree
        if age % 5 != 0:
            continue
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            new_tree_list.append([1,nx,ny])
    return new_tree_list + tree_list

def winter(ground,array_A):
    for i in range(n):
        for j in range(n):
            ground[i][j] += array_A[i][j]

tree_list.sort()

for _ in range(k):    
    tree_list, dead_tree = spring(ground,tree_list)
    summer(ground,dead_tree)
    tree_list = autumn(tree_list)
    winter(ground,array_A)

answer = len(tree_list)

print(answer)