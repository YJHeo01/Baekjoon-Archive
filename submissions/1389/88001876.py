#질문게시판 질문 피드백용 제출
import sys
input = sys.stdin.readline

from collections import deque

N, M = tuple(map(int, input().split()))

f = []
for i in range(N + 1):
    f.append([0] * (N + 1))

for i in range(M):
    l, r = tuple(map(int, input().split()))
    f[l][r] = 1
    f[r][l] = 1

min_c = N * N
min_i = 1
for i in range(1, N + 1):
    q = deque()
    q.append(i)
    c = [0] * (N + 1)
    v = [False] * (N + 1)
    v[i] = True
    while q:
        n = q.popleft()
        for j in range(1, N + 1):
            if not v[j] and f[n][j]:
                c[j] = c[n] + 1
                v[j] = True
                q.append(j)
    if min_c > sum(c):
        min_c = sum(c)
        min_i = i
print(min_i)