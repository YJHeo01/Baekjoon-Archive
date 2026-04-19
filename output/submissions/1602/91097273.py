import sys, heapq

input = sys.stdin.readline

INF = int(1e11)

def main():
    monkey = [0] + list(map(int,input().split()))
    time = [[INF]*(n+1)for _ in range(n+1)]
    delay_time = [[0]*(n+1) for _ in range(n+1)]
    set_init(time,monkey,delay_time)
    floyd(time,delay_time,monkey)
    print_answer(time)

def set_init(answer,monkey,delay_time):
    for i in range(1,n+1): answer[i][i] = monkey[i]
    for i in range(1,n+1):
        for j in range(1,n+1):
            delay_time[i][j] = max(monkey[i],monkey[j])
    for _ in range(m):
        a,b,d = map(int,input().split())
        answer[a][b] = min(answer[a][b],d + delay_time[a][b])
        answer[b][a] = answer[a][b]

def floyd(time,delay_time,monkey):
    q = []
    for i in range(1,n+1):
        heapq.heappush(q,(monkey[i],i))
    while q:
        tmp,k = heapq.heappop(q)
        for i in range(1,n+1):
            for j in range(1,n+1):
                path_i_to_k = time[i][k] - delay_time[i][k]
                path_k_to_j = time[k][j] - delay_time[k][j]
                if time[i][j] > path_i_to_k + path_k_to_j + max(monkey[k],delay_time[i][j]):
                    delay_time[i][j] = max(delay_time[i][j],monkey[k])
                    time[i][j] = path_i_to_k + path_k_to_j + delay_time[i][j]
                    continue
                if time[i][j] == path_i_to_k + path_k_to_j + max(monkey[k],delay_time[i][j]) and monkey[k] > delay_time[i][j]: delay_time[i][j] = monkey[k]
                    
def print_answer(time):
    for _ in range(q):
        a,b = map(int,input().split())
        answer = time[a][b]
        if answer >= INF: answer = - 1
        print(answer)

if __name__ == "__main__":
    n,m,q = map(int,input().split())
    main()