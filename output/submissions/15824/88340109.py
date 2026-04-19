import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = sorted(list(map(int,input().split())))
    answer = 0
    for i in range(n):
        for j in range(i):
            answer += (2 ** (i-j-1)) * (array[i]-array[j])
    print(answer)
        
if __name__ == "__main__":
    main()