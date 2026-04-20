import sys

from collections import deque

input = sys.stdin.readline

def check_finish(a,b):
    if a+b==0:
        return True
    else:
        return False

def check_tree(visited,start):
    tree = 1
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == False:
                if i == start:
                    tree = 0
                visited[i] = True
                queue.append(i)
    return tree



test_case_num = 0
while 1:
    tree_cnt = 0
    test_case_num += 1
    n,m = map(int,input().split())
    finish = check_finish(n,m)
    if finish == True:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
    visited = [False] * (n+1)
    for i in range(1,n+1):
        if visited[i] == False:
            tree_cnt += check_tree(visited,i)
    print("Case " + str(test_case_num) + ":",end=" ")
    if tree_cnt == 0:
        print("No trees.")
    elif tree_cnt == 1:
        print("There is one tree.")
    else:
        print("A forest of " + str(tree_cnt) + " trees.")