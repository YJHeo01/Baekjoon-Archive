import sys

input = sys.stdin.readline

def main():
    n = int(input())
    num_cnt = [0] * 10001
    for _ in range(n):
        num_cnt[int(input())] += 1
    for i in range(1,10001):
        for _ in range(num_cnt[i]):
            print(i)

if __name__ == "__main__":
    main()