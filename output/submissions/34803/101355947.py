l,n = map(int,input().split())

s = []

for _ in range(n):
    s.append(input())
    
k = int(input())

word = dict()

for i in range(n):
    for j in range(l-k+1):
        target = s[i][j:j+k]
        if target in word: word[target] += 1
        else: word[target] = 1

answer = 0

for c in word:
    answer = max(answer,word[c])

print(answer)