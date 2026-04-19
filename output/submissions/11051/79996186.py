import sys

sys.setrecursionlimit(10**6)

n,k = map(int,input().split())

def solution(value,k):
    if value == k: return 1
    return (value * solution(value-1,k) // (value-k)) % 10007

print(solution(n,k))
