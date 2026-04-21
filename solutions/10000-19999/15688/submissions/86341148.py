import sys
input = sys.stdin.readline
INF = 1000000
cnt = [0]*(2*INF+1)
for _ in range(int(input())):cnt[int(input())+INF]+=1
for i in range(2*INF+1):
    for _ in range(cnt[i]): print(i-INF)