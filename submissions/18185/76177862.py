n = int(input())

array = list(map(int,input().split()))

answer = 0

while True:
    stop = True
    for i in range(n-2):
        tmp = min(array[i:i+3])
        if tmp != 0:
            stop = False
            for j in range(i,i+3):
                array[j] -= 1
            answer += 7
    if stop == True:
        break

while True:
    stop = True
    for i in range(n-1):
        tmp = min(array[i:i+2])
        if tmp != 0:
            stop = False
            for j in range(i,i+2):
                array[j] -= 1
            answer += 5
    if stop == True:
        break

for i in range(n):
    answer += array[i] * 3

print(answer)