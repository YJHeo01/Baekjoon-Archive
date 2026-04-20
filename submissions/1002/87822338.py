def main():
    t = int(input())
    for _ in range(t):
        x1,y1,r1,x2,y2,r2 = map(int,input().split())
        if x1 == y1 and x2 == y2 and r1 == r2:
            print(-1)
        else:
            d = (x1-x2) ** 2 + (y1-y2) ** 2
            if d > (r1+r2) ** 2 or (x1 == x2 and y1 == y2):
                print(0)
            elif d < (r1+r2) ** 2:
                print(2)
            else:
                print(1)
        
if __name__ == "__main__":
    main()