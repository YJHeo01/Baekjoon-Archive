#https://github.com/YJHeo01

L,R = map(int,input().split())

def check_digit(num):
    digit = 0
    while num > 0:
        digit += 1
        num = num // 10
    return digit

answer = 0

if check_digit(L) == check_digit(R):
    L_stack = []
    while L > 0:
        L_stack.append(L%10)
        L = L // 10
    R_stack = []
    while R > 0:
        R_stack.append(R%10)
        R = R // 10
    while L_stack != []:
        if L_stack.pop() == 8 and R_stack.pop() == 8:
            answer += 1
        else:
            break
print(answer)