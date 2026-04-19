k = int(input())

answer = ''

while k > 0:
    k -= 1
    if k % 2 == 0: answer = '4' + answer
    else: answer = '7' + answer
    k //= 2
    
print(answer)