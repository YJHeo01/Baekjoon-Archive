import sys

input = sys.stdin.readline

def main():
    n = int(input())
    max_x, max_y = -10001, -10001
    min_x, min_y = 10001, 10001
    for _ in range(n):
        x,y = map(int,input().split())
        max_x, max_y = max(max_x,x), max(max_y,y)
        min_x, min_y = min(min_x,x), min(min_y,y)
    w,h = max_x - min_x, max_y - min_y
    if w == 0 or h == 0:print(0)
    else:print(w*h)

if __name__ == "__main__":
    main()