import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    for _ in range(k):
        a,b,c = map(int,input().split())
        for i in range(a-1,b):
            array[i] += c
        array.sort()
    print(*array)

if __name__ == "__main__":
    main()