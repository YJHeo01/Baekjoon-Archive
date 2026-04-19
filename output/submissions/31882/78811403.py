n = int(input())

s = list(input())

answer = 0
two_length = 0
for i in range(n):
    if s[i] == '2':
        two_length += 1
    else:
        for value in range(1,two_length+1):
            for _ in range(two_length+1-value):
                answer += value
        two_length = 0
print(answer)