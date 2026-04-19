INF = int(1e9)

def main():
    tc = int(input())
    for _ in range(tc):
        n,m,w = map(int,input().split())
        edges = get_road(m)
        edges += get_hole(w)
        answer = solution(edges,n)
        print(answer)

def get_road(m):
    ret_value = []
    for _ in range(m):
        s,e,t = map(int,input().split())
        ret_value.append((s,e,t))
        ret_value.append((e,s,t))
    return ret_value

def get_hole(w):
    ret_value = []
    for _ in range(w):
        s,e,t = map(int,input().split())
        ret_value.append((s,e,-t))
    return ret_value

def solution(edges,n):
    for start in range(1,n+1):
        answer = bellman_ford(edges,start,n)
        if answer == 'YES': return answer
    return answer

def bellman_ford(edges,start,n):
    distance = [INF] * (n+1)
    distance[start] = 0
    for _ in range(n):
        for mid, end, time in edges:
          if distance[mid] == INF: continue
          if distance[end] > distance[mid] + time:
              distance[end] = distance[mid] + time
    if distance[start] < 0: return 'YES'
    return 'NO'

if __name__ == "__main__":
    main()