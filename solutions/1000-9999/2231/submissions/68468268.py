n = int(input())
answer = 0
for i in range(1,n):
    tmp = i % 10
    for j in range(1,8):
        tmp += ((i%(10**(j+1))-i%(10**j)) //( 10 ** j))
    tmp += i
    if tmp == n:
        answer = i
        break

print(answer)
