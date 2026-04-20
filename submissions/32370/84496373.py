a,b = map(int,input().split())
x,y = map(int,input().split())

answer = 2

if a == 0:
    if x == 0 and b > y:
        answer = 3
    else:
        answer = 1

if b == 0:
    if y == 0 and x < a:
        answer = 3
    else:
        answer = 1

print(answer)