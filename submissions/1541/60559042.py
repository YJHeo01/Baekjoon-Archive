string = input()
sign = []
number = []
index = 0
for i in range(len(string)):
    if (string[i] == '+') or (string[i]=='-'):
        n = int(string[index:i])
        number.append(n)
        sign.append(string[i])
        index = i+1
    
n = int(string[index:len(string)])
number.append(n)
numbers = []
for j in range(len(sign)):
    if sign[j] == '+':
        if number[j] == 0:
            n = numbers.pop()
            n += number[j+1]
            numbers.append(n)
            number[j+1] = 0
        else:
            n = number[j] + number[j+1]
            numbers.append(n)
            number[j+1] = 0
    elif j == 0:
        numbers.append(number[j])

if sign[-1] == '-': numbers.append(number[-1])

answer = numbers.pop(0)
for k in range(0,len(numbers)):
    answer -= numbers[k]
    
print(answer)