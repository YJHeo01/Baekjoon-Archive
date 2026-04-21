n = int(input())

data = dict()

for _ in range(n):
    word = list(input())
    digit = 0
    while True:
        if word == []:
            break
        c = word.pop()
        if c not in data:
            data[c] = 0
        data[c] += 10 ** digit
        digit += 1

data = list(data.values())
data.sort(reverse=True)
answer = 0
num = 9
for x in data:
    answer += x * num
    num -= 1

print(answer)