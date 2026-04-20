n, c = map(int,input().split())

thing = list(map(int,input().split()))
answer = 0
for i in range(1,n+1):
    tmp = sum(thing[0:i])
    if tmp > c : 
        answer = i
        break
    for j in range(n-i):
        tmp -= thing[j]
        tmp += thing[j+i]
        if tmp > c: 
            answer = i
            break
    if answer != 0:
        break
print(answer)