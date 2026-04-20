import sys

input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        array = list(map(int,input().split()))
        cnt = {}
        for i in array[1:]:
            if i not in cnt: cnt[i] = 1
            else: cnt[i] += 1
        answer = "SYJKGW"
        for i in cnt:
            if cnt[i] > array[0] // 2:
                answer = i
                break
        print(answer)

if __name__ == "__main__":
    main()