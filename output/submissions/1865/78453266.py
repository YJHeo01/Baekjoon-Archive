import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    tc = int(input())
    for _ in range(tc):
        n,m,w = map(int,input().split())
        edges = get_road(m)
        edges += get_hole(w)
        distance = [INF] * (n+1)
        answer = get_answer(edges,distance,n)
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

def get_answer(edges,distance,n):
    distance[n] = 0
    for i in range(n):
        for mid, end, time in edges:
          if distance[end] > distance[mid] + time:
              if i == n-1: return 'YES'
              distance[end] = distance[mid] + time
    return 'NO'

if __name__ == "__main__":
    main()