import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        a,b = map(int,input().split())
        while True:
            if a > b:
                a = a // 2
            elif b > a:
                b = b // 2
            else:
                print(a*10)
                break
    
if __name__ == "__main__":
    main()