import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = [int(input()) for _ in range(n)]
    parent = list(range(n))
    answer = 0
    q = []
    visited = [False] * n
    for i in range(1,n):
        heapq.heappush(q,(max(array[i-1],array[i]),i-1,i))
    while q:
        value, left, right = heapq.heappop(q)
        if visited[left]: continue
        if max(array[find_parent(parent,left)], array[find_parent(parent,right)]) != value: continue
        answer += value
        visited[left] = True
        union_parent(array,parent,left,right)
        if right + 1 < n and visited[right] == False:
            heapq.heappush(q,(max(value,array[find_parent(parent,right+1)]),right,right+1))
        if left != 0 and visited[left-1] == False:
            heapq.heappush(q,(max(value,array[find_parent(parent,left-1)]),left-1,left))
    print(answer)

def union_parent(array,parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if array[a] >= array[b]:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main()