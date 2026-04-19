import sys; input = sys.stdin.readline
INF = int(1e9) + 7
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(5)
        continue
    answer = 4
    for _ in range(n-1):
        answer *= 5
        answer %= INF
    print(answer)