import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    distance_sum = 0
    point_list = [[] for _ in range(n)]
    for _ in range(m):
        tmp = list(map(int,input().split()))
        for i in range(n):
            point_list[i].append(tmp[i])
    position = []
    for i in range(n):
        if m % 2 == 1:
            position.append(point_list[i][m//2])
        else:
            position.append((point_list[i][m//2]+point_list[i][m//2-1])//2)
    for i in range(n):
        for j in range(m):
            distance_sum += abs(position[i]-point_list[i][j])
    print(distance_sum)
    print(*position)

if __name__ == "__main__":
    main()