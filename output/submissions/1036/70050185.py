def input_number(num_list):
    ret_v = 0
    n = int(input())
    for _ in range(n):
        tmp = list(input())
        tmp.reverse()
        digit = 0
        for c in tmp:
            num_list[digit].append(c)
            digit+=1
        ret_v = max(ret_v,digit)
    return ret_v

def search_sum_value(length):
    ret_v = 0
    for i in range(length,-1,-1):
        for num in num_list[i]:
            if ord(num) >= ord('A'):
                ret_v += (ord(num)-ord('A')+10)*(36**i)
            else:
                ret_v += int(num) * (36**i)
    return ret_v

def search_max_plus(k):
    value_change_plus = [0]*36
    for i in range(length,-1,-1):
        for num in num_list[i]:
            if ord(num) >= ord('A'):
                value_change_plus[ord(num)-ord('A')+10] += (35-(ord(num)-ord('A')+10))*(36**i)
            else:
                value_change_plus[int(num)] += (35-int(num))*(36**i)
    value_change_plus.sort(reverse=True)
    return sum(value_change_plus[0:k])

def search_digit(sum_value):
    digit = 1
    while 1:
        if sum_value < 36 ** digit:
            digit -= 1
            break
        digit += 1
    return digit

def search_answer(sum_value):
    ret_v = []
    digit = search_digit(sum_value)
    for i in range(digit,-1,-1):
        tmp = sum_value // (36**i)
        sum_value -= tmp * (36**i)
        if tmp >= 10:
            ret_v.append(chr(ord('A')+tmp-10))
        else:
            ret_v.append(str(tmp))
    return ret_v

num_list = [[]for _ in range(50)]
length = input_number(num_list) - 1
sum_value = search_sum_value(length)
k = int(input())
sum_value += search_max_plus(k)
answer = search_answer(sum_value)

for c in answer:
    print(c,end="")