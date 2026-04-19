import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    array = []
    value = 0
    cnt = 0
    for i in range(1,m+1):
        v = int(input())
        if v > 2 * n: continue
        if v >= n:
            print(1)
            print(i)
            return
        if value + v > 2 * n: continue
        cnt += 1
        value += v
        array.append(i)
        if value >= n: break
    print(cnt)
    for i in array:
        print(i)
        
if __name__  == "__main__":
    main()