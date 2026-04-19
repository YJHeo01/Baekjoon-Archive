n = int(input())
array= list(input())
answer = 0
couple = False
for i in range(n):
    if array[i] == 'S':
        answer += 1
        couple = False
    else:
        if couple == False:
            answer += 2
            couple = True

print(answer)