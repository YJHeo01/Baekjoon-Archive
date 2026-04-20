from collections import deque

t = int(input())

def check_num(c):
    if ord('0') <= ord(c) and ord(c) <= ord('9'):
        return True
    else:
        return False

def check_error(array,command):
    for c in command:
        if c == 'R':
            array.reverse()
        else:
            if array == deque([]):
                return True
            else:
                array.popleft()
    return False

for _ in range(t):
    command = list(input())
    n = int(input())
    tmp = list(input())
    l = len(tmp)
    array = deque([])
    for i in range(1,l):
        if check_num(tmp[i]) == True:
            if check_num(tmp[i-1]) == True:
                array[-1] *= 10
                array[-1] += int(tmp[i])
            else:
                array.append(int(tmp[i]))
    if check_error(array,command) == True:
        print("error")
    else:
        print("[",end="")
        while array:
            num = array.popleft()
            print(num,end="")
            if array != deque([]):
                print(',',end="")
        print("]")