n = list(input())

length = len(n)

if length % 2 == 1:
    print(-1)
    exit(0)

answer = ''

last_value = -1

for i in range(0,length,2):
    cnt = int(n[i])
    value = n[i+1]
    if cnt == 0:
        answer = -1
        break
    if last_value == value:
        answer = -1
        break
    for _ in range(cnt):
        answer += value
    last_value = value
        
if answer != -1 and answer[0] == '0': answer = -1

print(answer)