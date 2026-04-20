n = int(input())

a = list(map(int,input().split()))

answer = 0

A_i_value = 0

for i in a:
    if i > A_i_value:
        A_i_value = i
        answer += 1

print(answer)