text = list(input())

length = len(text)

answer = 0

idx = 0

while True:
    if idx >= length:
        break
    if idx + 1 < length:
        if text[idx] == 'c':
            if text[idx+1] == '-' or text[idx+1] == '=':
                idx += 2
            else:
                idx += 1
        elif text[idx] == 'd':
            if text[idx+1] == '-':
                idx += 2
            elif idx + 2 < length and text[idx+1] == 'z' and text[idx+2] == '=':
                idx += 3
            else:
                idx += 1
        elif text[idx+1] == 'j':
            if text[idx] == 'l' or text[idx] == 'n':
                idx += 2
            else:
                idx += 1
        elif text[idx+1] == '=':
            if text[idx] == 's' or text[idx] == 'z':
                idx += 2
            else:
                idx += 1
        else:
            idx += 1
    else:
        idx += 1
    answer += 1

print(answer)