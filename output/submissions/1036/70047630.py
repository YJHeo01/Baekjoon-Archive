n = int(input())
num_list = [[]for _ in range(50)]
change_num_list = ['Z']
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
    num_list[i].sort()
    for num in num_list[i]:
        if num in change_num_list:
            sum_value += 35*(36**i)
        elif k == 0:
            if ord(num) < ord('A'):
                sum_value += int(num) * (36**i)
            else:
                sum_value += (ord(num)-ord('A')+10)*(36**i)
        else:
            k-=1
            change_num_list.append(num)
            sum_value += 35*(36**i)
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