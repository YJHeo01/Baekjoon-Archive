import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    sum_value = 0
    one_cnt = 0
    for i in range(n):
        sum_value += array[i]
        one_cnt += array[i] % 2
    if sum_value % 3 != 0 or one_cnt > sum_value // 3:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()