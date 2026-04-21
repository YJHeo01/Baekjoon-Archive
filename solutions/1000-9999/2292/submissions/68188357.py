n = int(input())
cnt = 1
sum = 1
while(1):
    sum = sum + 6*(cnt-1)
    if n <= sum:
        break
    cnt += 1

print(cnt)