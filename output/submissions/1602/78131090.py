import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    monkey = [0] + list(map(int,input().split()))
    answer = [[INF]*(n+1)for _ in range(n+1)]
    delay_time = [[0]*(n+1) for _ in range(n+1)]
    move_time = set_init(answer,monkey,delay_time)
    floyd(move_time,answer,delay_time,monkey)
    print_answer(answer)

def set_init(answer,monkey,delay_time):
    move_time = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        move_time[i][i] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            delay_time[i][j] = max(monkey[i],monkey[j])
    for _ in range(m):
        a,b,d = map(int,input().split())
        move_time[a][b], move_time[b][a] = d, d
        answer[a][b] = move_time[a][b] + delay_time[a][b]
        answer[b][a] = answer[a][b]
    return move_time

def floyd(move_time,answer,delay_time,monkey):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if move_time[i][k]+move_time[k][j]+max(monkey[k],delay_time[i][j]) >= answer[i][j]:
                    continue
                delay_time[i][j] = max(delay_time[i][j],monkey[k])
                move_time[i][j] = min(move_time[i][j],move_time[i][k]+move_time[k][j])
                answer[i][j] = move_time[i][j]+ delay_time[i][j]             
                    
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