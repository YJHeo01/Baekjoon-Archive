import sys
input = sys.stdin.readline
INF = 1000001
cnt = [0]*INF
for _ in range(int(input())):cnt[int(input())]+=1
for i in range(INF):
    for _ in range(cnt[i]): print(i)