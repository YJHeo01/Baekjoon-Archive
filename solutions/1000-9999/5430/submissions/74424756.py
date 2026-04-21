t = int(input())

for _ in range(t):
    p = list(input())
    num_cnt = int(input())
    sentence = list(input())
    array = []
    tmp = -1
    error = False
    for c in sentence:
        if str.isdigit(c) == True:
            if tmp == -1:
                tmp = int(c)
            else:
                tmp = tmp * 10 + int(c)
        else:
            if tmp == -1:
                continue
            array.append(tmp)
            tmp = -1
    for command in p:
        if command == 'R':
            array.reverse()
        else:
            if array == []:
                error = True
                break
            array = array[1:]
    if error == True:
        print("error")
    else:
        print('[',end="")
        for num in array:
            print(num,end="")
            if num == array[-1]:
                continue
            print(',',end="")
        print(']')