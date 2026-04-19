import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    monkey = [0] + list(map(int,input().split()))
    answer = [[INF]*(n+1)for _ in range(n+1)]
    delay_time = [[0]*(n+1) for _ in range(n+1)]
    set_init(answer,monkey,delay_time)
    floyd(answer,delay_time,monkey)
    print_answer(answer)

def set_init(answer,monkey,delay_time):
    for i in range(1,n+1):
        answer[i][i] = monkey[i]
    for i in range(1,n+1):
        for j in range(1,n+1):
            delay_time[i][j] = max(monkey[i],monkey[j])
    for _ in range(m):
        a,b,d = map(int,input().split())
        answer[a][b] = d + delay_time[a][b]
        answer[b][a] = answer[a][b]

def floyd(answer,delay_time,monkey):
    for k in range(1,n+1):
        for i in range(1,n+1):
            if answer[i][k] == INF: continue
            for j in range(1,n+1):
                path_i_to_k = answer[i][k] - delay_time[i][k]
                path_k_to_j = answer[k][j] - delay_time[k][j]
                if answer[i][j] > path_i_to_k + path_k_to_j + max(monkey[k],delay_time[i][j]):
                    delay_time[i][j] = max(delay_time[i][j],monkey[k])
                    answer[i][j] = path_i_to_k + path_k_to_j + delay_time[i][j]
                    
def print_answer(answer):
    for _ in range(q):
        a,b = map(int,input().split())
        value = answer[a][b]
        if value >= INF:
            value = - 1
        print(value)

if __name__ == "__main__":
    n,m,q = map(int,input().split())
    main()