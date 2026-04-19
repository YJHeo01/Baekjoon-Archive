import sys

sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    print(solution(n,0))

def solution(value,cnt):
    if value == 1:
        return cnt
    if value == 2 or value == 3: return cnt + 1
    return min(solution((value-value%3)//3,cnt+1+value%3),solution((value-value%2)//2,cnt+1+value%2))

if __name__ == "__main__":
    main()