r1, c1, r2, c2 = map(int,input().split())
answer = []
max_digit = 0
digit_list = []

def find_digit(value):
    ret_value = 0
    while value != 0:
        ret_value += 1
        value = value // 10
    return ret_value
for y in range(r1,r2+1):
    tmp = []
    digit_tmp = []
    for x in range(c1,c2+1):
        abs_x, abs_y = abs(x), abs(y)
        if abs_x > abs_y:
            if abs_x == -x:
                value = (2*abs_x+1)**2 + 2*x - (abs_x-y)
            else:
                value = (2*abs_x-1) ** 2 + abs_x - y
        else:
            if abs_y == y:
                value = (2*abs_y+1)**2 - (y-x)
            else:
                value = (abs_y*2)**2+1-(abs_y+x)
        tmp.append(value)
        digit_tmp.append(find_digit(value))
    max_digit = max(max_digit,max(digit_tmp))
    answer.append(tmp)
    digit_list.append(digit_tmp)
r = r2 - r1 + 1
c = c2 - c1 + 1

for i in range(r):
    for j in range(c):
        for k in range(digit_list[i][j],max_digit):
            print(" ",end="")
        print(answer[i][j],end=" ")
    print()