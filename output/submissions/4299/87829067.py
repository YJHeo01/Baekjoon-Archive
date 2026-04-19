#질문게시판 답변용
p, m = list(map(int, input().split()))
x = (p + m)
y = (p - m)
if x % 2 != 0 or y % 2 != 0:
    print(-1)
else:
    x //= 2; y //= 2
    if x < y: x,y = y,x
    print(x, y)