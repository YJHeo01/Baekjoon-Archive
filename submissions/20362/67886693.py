n, S = input().split()
n = int(n)
answer = ' '
chat = []
for i in range(n):
    nickname, text = input().split()
    if nickname == S : 
        answer = text
        break
    chat.append(text)

print(chat.count(answer))