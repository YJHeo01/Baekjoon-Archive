import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    answer = 'Yes'
    for i in range(n):
        if (array[i] - i) % k != 0:
            answer = 'No'
    print(answer)

if __name__ == "__main__":
    main()