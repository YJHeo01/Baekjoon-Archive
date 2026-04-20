import math

def main():
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    answer = 0
    for i in range(n):
        if A[i] >= B[i]:continue
        answer += math.ceil((B[i]-A[i])/30)
    print(answer)

if __name__ == "__main__":
    main()