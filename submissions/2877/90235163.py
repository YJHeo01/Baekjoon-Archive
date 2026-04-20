k = int(input())

tmp = 2

answer = ''

while True:
    if k % 2 == 1: 
        answer = '4' + answer
    else:
        answer = '7' + answer
    k -= tmp
    tmp *= 2
    if k <= 0: break
    
print(answer)