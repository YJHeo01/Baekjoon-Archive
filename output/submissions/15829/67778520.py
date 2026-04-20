n = int(input())

sentence = [0]*n

sentence = list(input())
sum = 0
for i in range(n):
    sum = sum + (ord(sentence[i]) - ord('a') + 1) * (31 ** (i))
answer = sum % 1234567891
print(answer)
