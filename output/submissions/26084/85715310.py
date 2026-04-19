import sys, math

input = sys.stdin.readline

def main():
    s = list(input().rstrip())
    cnt = {}
    n = int(input())
    for _ in range(n):
        c = list(input())[0]
        if c in cnt: cnt[c] += 1
        else: cnt[c] = 1
    for c in s:
        if c not in cnt:
            print(0)
            return
    s.sort()
    if s[0] == s[1] and s[1] == s[2]:
        print(math.comb(cnt[s[0]],3))
    elif s[0] == s[1]:
        print(math.comb(cnt[s[1]],2)*cnt[s[2]])
    elif s[1] == s[2]:
        print(math.comb(cnt[s[1]],2)*cnt[s[0]])
    else:
        print(cnt[s[0]]*cnt[s[1]]*cnt[s[2]])

if __name__ == "__main__":
    main()