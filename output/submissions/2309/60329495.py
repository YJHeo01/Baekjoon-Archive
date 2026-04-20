tall = []
for k in range(9):
    tmp = int(input())
    tall.append(tmp)

liar = sum(tall) - 100
status = 0
for i in range(8):
    for j in range(i+1,9):
        if (tall[i] + tall[j]) == liar:
            tall.remove(tall[j])
            tall.remove(tall[i])
            tall.sort()
            status = 1
            break
    if status == 1:
        break

            
print(tall)    


