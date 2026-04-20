import math

def main():
    idx = 0
    while True:
        a,b,c = map(int,input().split())
        if a == 0 and b == 0 and c == 0:
            break
        idx += 1
        print("Triangle #" + str(idx))
        if a == 0 or b == 0 or c == 0:
            print("Impossible.")
            continue
        if a == -1:
            if b >= c:
                print("Impossible.")
                continue
            a = math.sqrt(c**2-b**2)
            print("a = {:.3f}".format(a))
        elif b == -1:
            if a >= c:
                print("Impossible.")
                continue
            b = math.sqrt(c**2-a**2)
            print("b = {:.3f}".format(b))
        else:
            print("c = {:.3f}".format(math.sqrt(a**2+b**2)))
        print()
        

if __name__ == "__main__":
    main()