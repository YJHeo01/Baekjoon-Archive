x,y = map(int,input().split())
answer = 1012 * x - 506 * y
if 2*x < y or y < x:
    answer = -1
print(answer)