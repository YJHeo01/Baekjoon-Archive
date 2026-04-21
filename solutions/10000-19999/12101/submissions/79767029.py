import sys

sys.setrecursionlimit(10**6)

def main():
    state = solution([],0,1)
    if state > 0:
        print(-1)

def solution(answer,sum_value,idx):
    if sum_value == n:
        if idx != k:
            return idx + 1
        l = len(answer)
        for i in range(l):
            print(answer[i],end="")
            if i != l-1:print('+',end="")
        print()
        return 0
    for i in range(1,4):
        if sum_value + i > n: break
        idx = solution(answer+[i],sum_value+i,idx)
        if idx <= 0: return idx
    return idx

if __name__  == "__main__":
    n,k = map(int,input().split())
    main()