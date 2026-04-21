import sys

input = sys.stdin.readline

def main():
    n = int(input())
    team = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        tmp = list(map(int,input().split()))
        graph[i] += tmp[1:]
    for i in range(1,n+1):
        if team[i] == -1: 
            if i == 1: team[i] = 0
            else: team[i] = 1
        for j in graph[i]:
            team[j] = (team[i]+1) % 2
    blue = []; white = []
    blue_cnt, white_cnt = 0,0
    for i in range(1,n+1):
        if team[i] == 0:
            blue.append(i); blue_cnt += 1
        else:
            white.append(i); white_cnt += 1
    print(blue_cnt)
    print(*blue)
    print(white_cnt)
    print(*white)

if __name__ == "__main__":
    main()