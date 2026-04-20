n = int(input())

def solution(target,n):
    if n == 0: return 1
    return n * solution(target,n-1)

print(solution(n,n))