import sys

input = sys.stdin.readline

try:
    while True:
        n,m = map(int,input().split())
        child_cnt = [0] * (n+1)
        for _ in range(m):
            a,b = map(int,input().split())
            child_cnt[a] += 1
            child_cnt[b] += 1
        answer = "NO"
        for i in range(n+1):
            if child_cnt[i] >= 4:
                answer = "YES"
        print(answer) 
except:
    exit()