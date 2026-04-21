w,h,x,y,p = map(int,input().split())

answer = 0

r = h // 2
def solution():
    a,b = map(int,input().split())
    if (a-x) ** 2 + (b-(y+r)) ** 2 <= r ** 2: return 1
    if (a-(x+w)) ** 2 + (b-(y+r)) ** 2 <= r ** 2: return 1
    if a < x or b < y or a > x + w or b > y + h: return 0
    return 1

for _ in range(p):
    answer += solution()

print(answer)