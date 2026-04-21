import sys

input = sys.stdin.readline

def main():
    q = int(input())
    for _ in range(q):
        ta,tb,va,vb = map(int,input().split())
        dohoon, sanghyuk = 0,tb * vb
        for _ in range(va):
            if dohoon <= sanghyuk:
                dohoon += ta
            else:
                sanghyuk += ta
        print(max(dohoon,sanghyuk))

if __name__ == "__main__":
    main()