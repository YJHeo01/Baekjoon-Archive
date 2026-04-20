x,y,w,s = map(int,input().split())

if 2*w <= s:
    print(x*w+y*w)
elif w <= s:
    tmp = min(x,y)
    print(tmp*s+(x+y-2*tmp)*w)
else:
    tmp = min(x,y)
    answer = tmp*s
    x -= tmp
    y -= tmp
    if x % 2 == 1:
        answer += w
        x -= 1
    if y % 2 == 1:
        answer += w
        y -= 1
    answer += (x+y) * s
    print(answer)