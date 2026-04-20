from collections import deque

n,m,k = map(int,input().split())

array_A = []

for _ in range(n):
    array_A.append(list(map(int,input().split())))

tree_list = [[deque([])for _ in range(n)]for _ in range(n)]

for _ in range(m):
    x,y,z = map(int,input().split())
    x -= 1; y -= 1
    tree_list[x][y].append(z)


nourishment = [[5]*n for _ in range(n)]

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,-1,1,-1,1]

for _ in range(k):

    dead_tree = []
    live_tree = []
    for x in range(n): #봄
        for y in range(n):
            while tree_list[x][y]:
                z = tree_list[x][y].popleft()
                if nourishment[x][y] >= z:
                    nourishment[x][y] -= z
                    live_tree.append([x,y,z+1])
                else:
                    dead_tree.append([x,y,z])
                    
    for x,y,z in dead_tree: #여름
        new_nourishment = z // 2
        nourishment[x][y] += new_nourishment
    tree_list = [[deque([])for _ in range(n)]for _ in range(n)]

    for x,y,z in live_tree: #가을
        if z % 5 == 0:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                tree_list[nx][ny].append(1)            
    for x,y,z in live_tree:
        tree_list[x][y].append(z)

    for i in range(n): #겨울
        for j in range(n):
            nourishment[i][j] += array_A[i][j]

answer = 0

for i in range(n):
    for j in range(n):
        while tree_list[i][j]:
            tmp = tree_list[i][j].popleft()
            answer += 1

print(answer)