n = int(input())
m = int(input())

array = list(input())

Pn_list = [0] * m
answer = 0

if array[0:3] == "IOI":
    Pn_list[1] = 1
    
for i in range(2,m-1):
    if array[i] == 'O':
        if array[i+1] == 'I' and array[i-1] == 'I':
            Pn_list[i] = Pn_list[i-2] + 1
            if Pn_list[i] >= n:
                answer += 1

print(answer)