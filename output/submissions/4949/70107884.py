def check_finish(string):
    if string[0] == '.':
        return True
    return False

def append_stack(stack,c):
    if c == '(':
        stack.append(')')
    else:
        stack.append(']')

def pop_stack(stack,c):
    if stack == []:
        return 'no'
    stack_pop = stack.pop()
    if stack_pop != c:
        return 'no'
    return 'yes'

def control_stack(stack,c):
    return_value = 'yes'
    if c == '(' or c == '[':
        append_stack(stack,c)
    elif c == ')' or c == ']':
        return_value = pop_stack(stack,c)
    else:
        return 'yes'
    return return_value

while 1:
    answer = 'yes'
    stack = []
    string = list(input())
    finish = check_finish(string)
    if finish == True:
        break
    for c in string:
        if c == ' ':
            continue
        answer = control_stack(stack,c)
        if answer == 'no':
            break
    if stack != []:
        answer ='no'
    print(answer)