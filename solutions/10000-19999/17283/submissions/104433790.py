l = int(input())
r = int(input())

last = int(l * r / 100)
cnt = 2

answer = last * cnt

while True:
    cur = int(last * (r/100))
    if cur <= 5: break
    cnt *= 2
    answer += cur * cnt
    last = cur
    
print(answer)