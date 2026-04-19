import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    answer = 0
    while True:
        if k == 1: break
        answer += 1
        n = n % 2 + n // 2
        k -= 1
    answer += n
    print(answer)

if __name__ == "__main__":
    main()