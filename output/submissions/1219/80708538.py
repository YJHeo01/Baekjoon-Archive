import sys

input = sys.stdin.readline

def main():
    n,s,e,m = map(int,input().split())
    edges = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges.append((a,b,c))
    array = list(map(int,input().split()))
    INF = int(1e9)
    distance = [-INF] * (n+1)
    distance[s] = array[s]
    if exist_cycle(array,edges,distance,n) == True:
        if distance[e] == -INF:
            print("gg")
        else:
            print("Gee")
    elif distance[e] == -INF:
        print("gg")
    else:
        print(distance[e])

def exist_cycle(array,edges,distance,n):
    for _ in range(n-1):
        for start, end, cost in edges:
            if distance[start] + array[end] - cost > distance[end]:
                distance[end] = distance[start] + array[end] - cost
    for start,end,cost in edges:
        if distance[start] + array[end] - cost > distance[end]:
            return True
    return False

if __name__ == "__main__":
    main()