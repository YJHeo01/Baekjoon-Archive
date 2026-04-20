n,c,w = map(int,input().split())

tree = [int(input()) for _ in range(n)]

answer = 0

for size in range(1,10001):
    tmp = 0
    for i in range(n):
        if size > tree[i]: continue
        tmptmp = (tree[i] // size) * size * w - c * (tree[i]//size)
        if tree[i] % size == 0: tmptmp += c
        if tmptmp > 0: tmp += tmptmp
    answer = max(answer,tmp)

print(answer)