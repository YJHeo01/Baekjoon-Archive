from collections import deque
import sys

input = sys.stdin.readline

def main():
    
    n = int(input())
    graph = [[] for _ in range(n+1)]
    son = [[-1]*2 for _ in range(n+1)]
    node = [0] * (n+1)
    
    for i in range(1,n+1):
        a,h = map(int,input().split())
        node[i] = a
        graph[h].append((a,i))
        #그래프의 인덱스를 a로 하면 a의 범위가 너무 커서 메모리 초과될 것으로 생각, 그래서 a값에 대응하는 인덱스, i를 따로 마련해줌
        #노드의 깊이를 기준으로 분류해서 그래프에 저장

    for i in range(1,n+1):
        graph[i].sort()#BST는 좌측 자식의 크기가 더 작고, 우측 자식의 크기가 더 큼

    if len(graph[1]) != 1:#루트가 1개가 아니면 올바르지 못한 트리
        print(-1)
        return

    for depth in range(1,n):
        if graph[depth+1] == []:#현재 깊이+1 노드가 없다는 것은 더이상 자식을 분류하지 않아도 됨
            break
        parent_s_length = len(graph[depth])
        son_s_length = len(graph[depth+1])
        parent_left, parent_right = 0,parent_s_length-1
        son_left,son_right = 0,son_s_length - 1
        
        while son_left < son_right:#line20의 정렬을 이 while문을 위한 정렬, 그리디하게 자식 노드를 배정
            if parent_left >= parent_s_length or parent_right < 0:
                print(-1)
                return
            son[graph[depth][parent_left][1]][0] = graph[depth+1][son_left][1]
            son[graph[depth][parent_right][1]][1] = graph[depth+1][son_right][1]
            son_left += 1; parent_left += 1
            son_right -= 1; parent_right -= 1
        
        if son_left == son_right:
            if parent_left >= parent_s_length or parent_right < 0:
                print(-1)
                return
            if graph[depth][parent_left][1] > graph[depth+1][son_left][1]:
                son[graph[depth][parent_left][1]][0] = graph[depth+1][son_left][1]
            elif graph[depth][parent_right][1] < graph[depth+1][son_right][1]:
                son[graph[depth][parent_right][1]][1] = graph[depth+1][son_right][1]
            else:
                print(-1)
                return
    
    #bfs는 이진 트리의 자식 노드가 올바르게 배정되었는지 확인
    visited = [False] * (n+1)
    if bfs(son,node,visited,graph[1][0][1]) == False: 
        print(-1)
        return
    
    #위 BFS를 통과했어도 부모 - 자식 - 손주 형태의 트리 중 손주는 존재하고 자식에 해당하는 노드가 존재하지 않을 경우 visited[i] == False가 발생 가능
    for i in range(1,n+1):
        if visited[i] == False:
            print(-1)
            return
    
    for i in range(1,n+1):
        print(*son[i])

def bfs(son,node,visited,start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vx = queue.popleft()
        nx = son[vx][0]
        if nx != -1:
            if node[vx] <= node[nx]: #좌측 자식 노드가 부모보다 더 클 경우 올바르지 않음
                return False
            visited[nx] = True
            queue.append(nx)
        nx = son[vx][1]
        if nx != -1:
            if node[nx] <= node[vx]: #우측 자식 노드가 부모보다 작을 경우 올바르지 않음
                return False
            visited[nx] = True
            queue.append(nx)
    return True

if __name__ == "__main__":
    main()