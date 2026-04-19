import sys; input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w,n = map(int,input().split())
    answer = 0
    trash = 0
    for _ in range(n):
        x_i, w_i = map(int,input().split())
        trash += w_i
        if trash > w:
            answer += x_i
            trash = w_i
    answer += x_i
    answer *= 2
    print(answer)