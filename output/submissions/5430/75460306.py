from collections import deque

t = int(input())

for _ in range(t):
    p = deque(list(input()))
    m = int(input())
    array = list(input())
    num_list = deque([])
    tmp = 0
    for i in array:
        if i.isdigit() == True:
            tmp *= 10
            tmp += int(i)
        else:
            num_list.append(tmp)
            tmp = 0
    num_list.popleft()
    if m == 0:
        num_list.popleft()
    error = False
    while p:
        command = p.popleft()
        if command == 'R':
            if p == deque([]):
                num_list.reverse()
                break
            elif p[0] == 'R':
                p.popleft()
            else:
                num_list.reverse()
        else:
            if num_list == deque([]):
                error = True
                break
            num_list.popleft()
    if error == True:
        print('error')
    else:
        print('[',end="")
        while num_list:
            value = num_list.popleft()
            print(value,end="")
            if num_list != deque([]):
                print(",",end="")
        print(']')