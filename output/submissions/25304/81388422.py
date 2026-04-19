import sys

input = sys.stdin.readline

def main():
    x = int(input())
    n = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        x -= a * b
    if x == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()