import sys

input = sys.stdin.readline

m = int(input())
k = int(input())
stone = list(map(int, input().split()))

stone = sorted(set(stone))
L = stone[-1]

LIMIT = 538

# m이 작으면 그냥 m까지 DP (사이클 탐지 X)
if m <= LIMIT:
    lose = [True] * (m + 1)
    lose[0] = True

    answer = 0
    for i in range(1, m + 1):
        lose[i] = True
        for s in stone:
            if s > i: break
            if lose[i - s] == True:
                lose[i] = False
                break
        if lose[i] == True:
            answer += 1

    print(answer)
    sys.exit(0)

# m이 크면: 538까지 만들고 사이클 찾아서 점프
lose = [True] * (LIMIT + 1)
lose[0] = True

dp = [0] * (LIMIT + 1)

seen = dict()

start = 0
period = 0
cnt = 0

for i in range(1, LIMIT + 1):
    lose[i] = True
    for s in stone:
        if s > i: break
        if lose[i - s] == True:
            lose[i] = False
            break

    dp[i] = dp[i - 1] + (1 if lose[i] else 0)

    if i >= L:
        key = tuple(lose[i - L + 1 : i + 1])
        if key in seen:
            p_i, p_cnt = seen[key]
            start = p_i
            period = i - p_i
            cnt = dp[i] - p_cnt
            break
        else:
            seen[key] = (i, dp[i])

answer = dp[start]

INF = period + 1
answer += cnt * ((m - start) // (INF - 1))

tmp = (m - start) % (INF - 1)
answer += dp[start + tmp] - dp[start]

print(answer)