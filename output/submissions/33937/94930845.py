s = [input() for _ in range(2)]

answer = ''

for i in range(2):
    
    idx = 0

    while True:
        if idx == len(s[i]):
            print('no such exercise')
            exit(0)
        if s[i][idx] in ['a','e','i','o','u']:
            break
        answer += s[i][idx]
        idx += 1

    while True:
        if idx == len(s[i]):
            print('no such exercise')
            exit(0)
        if s[i][idx] not in ['a','e','i','o','u']:
            break
        answer += s[i][idx]
        idx += 1
    
print(answer)