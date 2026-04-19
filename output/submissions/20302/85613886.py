import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    prime_idx_list = [-1] * INF
    factor_list = [[] for _ in range(INF)]
    length = init(prime_idx_list,factor_list,)
    prime_cnt = [0] * length
    n = int(input())
    array = ['*'] + list(input().split())
    for i in range(n):
        value = abs(int(array[2*i+1]))
        if value == 0:
            print("mint chocolate")
            return
        if value == 1: continue
        dfs(prime_idx_list,factor_list,value,prime_cnt,array[2*i])
    answer = 'mint chocolate'
    for i in range(length):
        if prime_cnt[i] < 0:
            answer = 'toothpaste'
    print(answer)


def init(prime_idx_list,factor_list):
    ret_value = 0
    prime_list = []
    visited = [False] * INF
    prime_check = [True] * INF
    prime_idx = 0
    for i in range(2,INF):
        if prime_check[i]:
            prime_idx_list[i] = prime_idx
            prime_idx += 1; factor = 1
            prime_list.append(i)
            for j in range(i,INF,i):
                prime_check[j] = False
                if visited[j]: continue
                factor_list[j] = [i,factor]
                visited[j] = True; factor += 1
            ret_value += 1
    return ret_value
    
def dfs(prime_idx_list,factor_list,cur_value,prime_cnt,command):
    if prime_idx_list[cur_value] != -1:
        if command == '*':
            prime_cnt[prime_idx_list[cur_value]] += 1
        else:
            prime_cnt[prime_idx_list[cur_value]] -= 1
        return
    for next_value in factor_list[cur_value]:
        dfs(prime_idx_list,factor_list,next_value,prime_cnt,command)

if __name__ == "__main__":
    INF = 100001
    main()