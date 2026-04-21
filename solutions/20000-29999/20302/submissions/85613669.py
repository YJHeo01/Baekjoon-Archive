import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    prime_list = []
    prime_check = [True] * (100001)
    prime_idx_list = [-1] * (100001)
    prime_idx = 0
    factor = [[] for _ in range(100001)]
    visited = [False] * 100001
    for i in range(2,100001):
        if prime_check[i]:
            prime_idx_list[i] = prime_idx
            prime_idx += 1
            prime_list.append(i)
            tmp = 1
            for j in range(i,100001,i):
                prime_check[j] = False
                if visited[j]: continue
                visited[j] = True
                factor[j] = [i,tmp]
                tmp += 1
    length = len(prime_list)
    prime_cnt = [0] * length
    n = int(input())
    array = ['*'] + list(input().split())
    for i in range(n):
        tmp = abs(int(array[2*i+1]))
        if tmp == 0:
            print("mint chocolate")
            return
        if tmp == 1: continue
        solution(prime_idx_list,factor,tmp,prime_cnt,array[2*i])
    answer = 'mint chocolate'
    for i in range(length):
        if prime_cnt[i] < 0:
            answer = 'toothpaste'
    print(answer)

def solution(prime_idx_list,factor,value,prime_cnt,command):
    if prime_idx_list[value] != -1:
        if command == '*':
            prime_cnt[prime_idx_list[value]] += 1
        else:
            prime_cnt[prime_idx_list[value]] -= 1
        return
    for next_value in factor[value]:
        solution(prime_idx_list,factor,next_value,prime_cnt,command)


if __name__ == "__main__":
    main()