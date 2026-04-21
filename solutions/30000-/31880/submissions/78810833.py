n,m = map(int,input().split())

lucky_A = list(map(int,input().split()))
lucky_B = list(map(int,input().split()))

answer = sum(lucky_A)

for i in lucky_B:
    if i == 0: continue
    answer *= i

print(answer)