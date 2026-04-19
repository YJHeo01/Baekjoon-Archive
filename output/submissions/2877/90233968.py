k = int(input()) - 1

digit = 1

tmp = 2

while True:
    if tmp > k: break
    digit += 1
    tmp += 1 << digit

answer = ''

for i in range(digit):
    if k & (1<<i):
        answer = '7' + answer
        
    else:
        answer = '4' + answer
    k -= 2 ** (i)
        
print(answer)