import sys

input = sys.stdin.readline

def main():
    n,l = map(int,input().split())
    array = list(map(int,input().split()))
    b = list(map(int,input().split()))
    t = 1
    no = 1
    for i in range(n):
        if b[i] == 1:
            if no % array[i] == 0:
                t = -1
                break
            gcd = euclidean(array[i],t)
            t = t * array[i] // gcd
        else:
            if t % array[i] == 0:
                t = -1
                break
            gcd = euclidean(array[i],no)
            no = no * array[i] // gcd

    if t > l or t % no == 0: t = -1
    print(t)


def euclidean(a,b):
    if b == 0: return a
    return euclidean(b,a%b)

if __name__ == "__main__":
    main()