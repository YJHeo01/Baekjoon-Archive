n = int(input())

array = list(map(int,input().split()))

answer = 0

while True:
    finish = True
    for i in range(n):
        if array[i] % 2 != 0:
            finish = False
            answer += 1
            array[i] -= 1
    multiple = False
    for i in range(n):
        if array[i] == 0:continue
        finish = False
        multiple = True
        array[i] = array[i] // 2
    if finish == True:break
    if multiple == True:answer += 1

print(answer)