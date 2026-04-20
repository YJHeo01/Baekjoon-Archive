n = int(input())
m = int(input())

array = list(input())

Pn_list = [0] * m
answer = 0
for i in range(1,m-1):
    if array[i] == 'O':
        if array[i+1] == 'I' and array[i-1] == 'I':
            if i < 2:
                Pn_list[i] = 1
            else:
                Pn_list[i] = Pn_list[i-2] + 1
            if Pn_list[i] >= n:
                answer += 1

print(answer)