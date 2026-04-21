n = int(input())

cnt = 0
answer = -1

arr = list(map(int,input().split()))

for a in range(-500,501):
    for b in range(-500,501):
        solve = True
        for i in range(1,n):
            if arr[i-1] * a + b != arr[i]:
                solve = False
                break
        if solve:
            tmp = arr[n-1] * a + b
            if answer == tmp and cnt != 0: continue
            cnt += 1
            answer = tmp

if cnt == 0:
    print('B')
elif cnt >= 2:
    print('A')
else:
    print(answer)