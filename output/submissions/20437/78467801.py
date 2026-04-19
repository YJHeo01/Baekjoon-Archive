import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s = list(input())
        k = int(input())
        solution(s,k)

def solution(s,k):
    shortest = 10001
    longest = -1
    length = len(s)
    for left in range(length):
        target = s[left]
        cnt = 0
        for right in range(left,length):
            if target == s[right]: cnt += 1
            if cnt == k:
                shortest = min(shortest,right-left+1)
                longest = max(longest,right-left+1)
                break
    if longest == -1:
        print(-1)
    else:
        print(shortest,longest)

if __name__ == "__main__":
    main()