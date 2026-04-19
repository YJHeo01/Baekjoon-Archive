import math

def main():
    t = int(input())
    for _ in range(t):
        x1,y1,r1,x2,y2,r2 = map(int,input().split())
        if x1 == x2 and y1 == y2 and r1 == r2:
            print(-1)
            continue
        dot_distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
        if dot_distance > (r1+r2):
            print(0)
        elif dot_distance == (r1+r2):
            print(1)
        else:
            if r1 < r2:
                x1,y1,r1,x2,y2,r2 = x2,y2,r2,x1,y1,r1
            if dot_distance < r1:
                if dot_distance + r2 < r1:
                    print(0)
                elif dot_distance + r2 > r1:
                    print(2)
                else:
                    print(1)
            else:
                print(2)

if __name__ == "__main__":
    main()