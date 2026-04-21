import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer = 1
    for i in range(n):
        tmp = euclidean(answer,array[i]*2)
        answer = answer * array[i] * 2 // tmp
    print(answer)

def euclidean(a,b):
    if b == 0: return a
    return euclidean(b,a%b)

if __name__ == "__main__":
    main()