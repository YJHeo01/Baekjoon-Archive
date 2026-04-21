n = int(input())
score = 0
for i in range(n):
    text = list(input())
    cnt = 1
    for j in range(len(text)):
        if text[j] == 'O':
            score += cnt
            cnt += 1
        else : cnt = 1
    print(score)
    score = 0