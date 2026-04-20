import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        a,b = map(int,input().split())
        x1, y1 = 0,1
        x2, y2 = 0,1
        for i in range(10000):
            tmp = (i+1) * (i+2) // 2
            if tmp >= a:
                x1, y1 = i+1, a - i * (i+1) // 2
                break
        for i in range(10000):
            tmp = (i+1) * (i+2) // 2
            if tmp >= b:
                x2, y2 = i+1, b - i * (i+1) // 2
                break
        #print(x1,y1)
        #print(x2,y2)
        x,y = x1 + x2, y1 + y2
        print(x*(x+1)//2+y) 

if __name__ == "__main__":
    main()