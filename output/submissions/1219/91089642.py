import sys

input = sys.stdin.readline

INF = int(1e20)

def main():
    edges = []
    visited = [False] * n
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges.append((a,b,c))
    array = list(map(int,input().split()))
    distance = [-INF] * (n+1)
    distance[s] = array[s]
    visited[s] = True
    if exist_cycle(array,edges,distance,visited) == True and visited[e] != False:
        print("Gee")
    elif visited[e] == False:
        print("gg")
    else:
        print(distance[e])

def exist_cycle(array,edges,distance,visited):
    for _ in range(n-1):
        for start, end, cost in edges:
            if visited[start] == False: continue
            visited[end] = True
            if distance[start] + array[end] - cost > distance[end]:
                distance[end] = distance[start] + array[end] - cost
    for _ in range(n**2+1):
        for start,end,cost in edges:
            if visited[start] == False: continue
            visited[end] = True
            if distance[start] + array[end] - cost > distance[end]: 
                if end == e: return True
                distance[end] = distance[start] + array[end] - cost
    return False

if __name__ == "__main__":
    n,s,e,m = map(int,input().split())
    main()