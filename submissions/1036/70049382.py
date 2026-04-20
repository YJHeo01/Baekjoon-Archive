n = int(input())
num_list = [[]for _ in range(50)]
value_change_plus = [0]*36
length = 0
for _ in range(n):
    tmp = list(input())
    tmp.reverse()
    digit = 0
    for c in tmp:
        num_list[digit].append(c)
        digit+=1
    length = max(length,digit)
k = int(input())
sum_value = 0


for i in range(length-1,-1,-1):
    for num in num_list[i]:
        if ord(num) >= ord('A'):
            sum_value += (ord(num)-ord('A')+10)*(36**i)
            value_change_plus[ord(num)-ord('A')+10] += (35-(ord(num)-ord('A')+10))*(36**i)
        else:
            sum_value += int(num) * (36**i)
            value_change_plus[int(num)] += (35-int(num))*(36**i)

value_change_plus.sort(reverse=True)

sum_value += sum(value_change_plus[0:k])
digit = 1

while 1:
    if sum_value < 36 ** digit:
        digit -= 1
        break
    digit += 1

answer = []

for i in range(digit,-1,-1):
    tmp = sum_value // (36**i)
    sum_value -= tmp * (36**i)
    if tmp >= 10:
        answer.append(chr(ord('A')+tmp-10))
    else:
        answer.append(str(tmp))

for c in answer:
    print(c,end="")