n,b = map(int,input().split())

array = list(map(int,input().split()))

b_idx = array.index(b)

answer = 0

left, right = b_idx, b_idx

balance = 0

while True:
    if left < 0 or right >= n: break
    move_left, move_right = False, False
    if balance == 0:
        answer += 1
        if left <= 0: right += 1; move_right = True
        else: left -= 1; move_left = True
    elif balance < 0:
        if right + 1 >= n: left -= 1; move_left = True
        elif left - 1 < 0: right += 1; move_right = True
        else:
            if array[right+1] < b: right += 1; move_right = True
            else: left -= 1; move_left = True
    else:
        if right + 1 >= n: left -= 1; move_left = True
        elif left - 1 < 0: right += 1; move_right = True
        else:
            if array[right+1] > b: right += 1; move_right = True
            else: left -= 1; move_left = True
    if left < 0 or right >= n: break
    if move_left:
        if array[left] < b: balance += 1
        else: balance -= 1
    else:
        if array[right] < b: balance += 1
        else: balance -= 1
        
print(answer)