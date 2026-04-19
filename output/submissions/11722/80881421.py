import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer = 1
    length = [1] * n
    for i in range(1,n):
        for j in range(i):
            if array[i] < array[j]:
                length[i] = max(length[i],length[j]+1)
                answer = max(answer,length[i])
    print(answer)

if __name__ == "__main__":
    main()