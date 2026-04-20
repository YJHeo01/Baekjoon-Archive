n = int(input())

digit = 1

tmp = 9

answer = 0

while True:
    if tmp > n: break
    dd = (digit+1) // 2
    if dd == 1:
        answer += 9 ** ((digit+1)//2)
    else:
        answer += 10 * (9**(dd-1))
    tmp *= 10
    tmp += 9
    digit += 1
    
def backtracking(value,cur_digit):
    if cur_digit == digit:
        if value[0] == '0' or int(value) > n: return 0
        else: return 1
    ret_value = 0
    for i in range(10):
        ret_value += backtracking(str(i)+value+str(i),cur_digit+2)
    return ret_value

if digit % 2 == 1:
    for i in range(10):
        answer += backtracking(str(i),1)
else:
    answer += backtracking('',0)
    
print(answer)