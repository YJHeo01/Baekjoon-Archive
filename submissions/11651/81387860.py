import sys

input = sys.stdin.readline

def main():
    n = int(input())
    point = []
    for _ in range(n):
        point.append(list(map(int,input().split())))
    point.sort(key=lambda x : (x[1],x[0]))
    for i in point:
        print(*i)

if __name__ == "__main__":
    main()