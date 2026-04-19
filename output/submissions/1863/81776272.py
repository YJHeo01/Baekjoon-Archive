import sys

input = sys.stdin.readline

def main():
    idx = 1
    visited = [0] * 500001
    n = int(input())
    answer = 0
    for _ in range(n):
        x,y = map(int,input().split())
        if y == 0: idx += 1
        else:
            if visited[y] != idx:
                visited[y] = idx
                answer += 1
    print(answer)

if __name__ == "__main__":
    main()