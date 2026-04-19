import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    distance = get_distance(n,m)
    distance = floyd(distance)
    print_answer(distance)

def get_distance(n,m):
    distance = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        distance[a][b], distance[b][a] = 1,1
    for i in range(n+1): distance[i][i] = 0
    return distance

def floyd(distance):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])
    return distance

def print_answer(distance):
    answer_L, answer_R, answer_D = 0,0,INF
    for i in range(1,n):
        for j in range(i+1,n+1):
            tmp = get_distance_sum(distance,i,j)
            if answer_D > tmp: answer_L, answer_R, answer_D = i,j,tmp
    answer_D *= 2
    print(answer_L,answer_R,answer_D)

def get_distance_sum(distance,i,j):
    ret_value = 0
    for mid in range(1,n+1): ret_value += min(distance[i][mid],distance[j][mid])
    return ret_value

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()