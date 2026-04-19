n,k = map(int,input().split())
level = sorted([int(input()) for _ in range(n)])
answer = level[0]
cnt = n

for i in range(1,n):
    if k >= (level[i] - level[i-1]) * i:
        k -= (level[i] - level[i-1]) * i
        answer = level[i]
    else:
        cnt = i
        break

if k != 0:
    answer += k // cnt

print(answer)