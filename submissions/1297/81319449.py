import math

def main():
    d,h,w = map(int,input().split())
    x = math.sqrt((d**2/(1+w**2/h**2)))
    y = x * w / h
    x,y = int(x), int(y)
    print(str(x) + " "+ str(y))

if __name__ == "__main__":
    main()